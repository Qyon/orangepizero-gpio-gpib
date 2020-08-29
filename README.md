# orangepizero-gpio-gpib
Orange Pi Zero GPIO GPIB interface

Based on http://elektronomikon.org/ project. https://github.com/elektronomikon/raspi_gpib_driver

Used:
- https://github.com/Qyon/gpib_network_server
- https://github.com/Qyon/raspi_gpib_driver
- https://linux-gpib.sourceforge.io/

# Armbian compile 

```./compile.sh BOARD=orangepizero BRANCH=current RELEASE=focal BUILD_MINIMAL=yes BUILD_DESKTOP=no KERNEL_ONLY=no INSTALL_HEADERS=yes KERNEL_CONFIGURE=no FIXED_IMAGE_SIZE=1024```
