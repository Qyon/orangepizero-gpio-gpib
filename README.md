# orangepizero-gpio-gpib
Orange Pi Zero GPIO GPIB interface

Based on http://elektronomikon.org/ project. https://github.com/elektronomikon/raspi_gpib_driver

Used:
- https://github.com/Qyon/gpib_network_server
- https://github.com/Qyon/raspi_gpib_driver
- https://linux-gpib.sourceforge.io/

# Armbian compile 

```./compile.sh BOARD=orangepizero BRANCH=current RELEASE=focal BUILD_MINIMAL=yes BUILD_DESKTOP=no KERNEL_ONLY=no INSTALL_HEADERS=yes KERNEL_CONFIGURE=no FIXED_IMAGE_SIZE=1024```

# Settings
- listens on port `5660` + GPIB device address
- hostname `opi-gpib.local`
- username:password root:1234
- example `connect.ini` for KE5FX GPIB Toolkit: 
```
interface_settings  ip.address.of.interface:5678 # for device id 18
is_Prologix          0
write_delay_ms       0
reset_to_local       1
force_auto_read      1
restore_auto_read    0
enable_lon           1
```
- ip.address.of.interface can easy be obtained on Windows 10 by: `ping opi-gpib.local`

# Design docs
https://workspace.circuitmaker.com/Projects/Details/Lukasz-Nidecki-2/opi-zero-gpib
