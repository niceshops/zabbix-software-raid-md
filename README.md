# Zabbix - Software Raid (MD) Monitoring

* Low-Level Discovers (auto-discover multiple MD RAIDs)

* Items
  * Software Raid {#MD_DEV} Active devices
  * Software Raid {#MD_DEV} Array level
  * Software Raid {#MD_DEV} Array size
  * Software Raid {#MD_DEV} Array update-time
  * Software Raid {#MD_DEV} Devices
  * Software Raid {#MD_DEV} Failed devices
  * Software Raid {#MD_DEV} Resync status
  * Software Raid {#MD_DEV} Spare devices
  * Software Raid {#MD_DEV} Status

* Triggers
  * Software RAID '{#MD_DEV}' disks are missing
  * Software RAID '{#MD_DEV}' has FAILED disks


## Install

1. Import the YAML Template into your Zabbix Server
2. Add the Userparameter (_also update the path to the script_)
3. Add the Script (_executable by Zabbix serviceuser_)
4. Add the sudoers file in /etc/sudoers.d/ to give the serviceuser permission to read the RAID information

## Test

```bash
root@server: sudo su zabbix --shell /bin/bash --login
zabbix@server: sudo /usr/sbin/mdadm --detail /dev/md1
```
