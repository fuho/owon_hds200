@echo off
echo win_ver_check
ver|find "6.2">nul&&goto :win8

:win8
devcon.exe rescan
rundll32 "%cd%\x86\libusb0_x86.dll,usb_install_driver_np_rundll usb_device.inf"