#!/usr/bin/env python3

from subprocess import Popen as subprocess_popen
from subprocess import PIPE as subprocess_pipe
from sys import argv as sys_argv
from json import dumps as json_dumps

try:
    CHECK = sys_argv[1]

except IndexError:
    raise SystemExit('You must specify the following arguments: 1 => check-type')


ZBX_KEY = '{#MD_DEV}'
CMD_STATS = 'sudo /usr/sbin/mdadm --detail /dev/'

if CHECK == 'discover':
    result = {'data': []}

    _stdout, _ = subprocess_popen(
        ['ls /dev | grep -E md[0-9]'],
        shell=True,
        stdout=subprocess_pipe,
        stderr=subprocess_pipe,
    ).communicate()
    md_devices = _stdout.decode('utf-8').strip().splitlines()

    for dev in md_devices:
        result['data'].append({ZBX_KEY: dev.strip()})

    print(json_dumps(result))

else:
    try:
        MD_DEV = sys_argv[2]
        if not MD_DEV.startswith('md'):
            raise ValueError(f"MD-Device must start with 'md' - got: {MD_DEV}!")

    except IndexError:
        raise SystemExit('You must specify the following arguments: 1 => check-type, 2 => md-device')

    filter_matching = {
        'status': 'State',
        'devs': 'Raid Devices',
        'active': 'Active Devices',
        'failed': 'Failed Devices',
        'spare': 'Spare Devices',
        'resync': 'Resync Status',
        'level': 'Raid Level',
        'size': 'Array Size',
        'updated': 'Update Time',
    }

    if CHECK not in filter_matching:
        raise ValueError(f"Unsupported check '{CHECK}'!")

    _stdout, _ = subprocess_popen(
        [f"{CMD_STATS}{MD_DEV} | grep '{filter_matching[CHECK]} :' | cut -d ':' -f 2"],
        shell=True,
        stdout=subprocess_pipe,
        stderr=subprocess_pipe,
    ).communicate()
    print(_stdout.decode('utf-8').strip())

