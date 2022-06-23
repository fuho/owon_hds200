if exist %SystemRoot%\system32 copy x86\libusb0_x86.dll %SystemRoot%\system32\libusb0.dll
if exist %SystemRoot%\syswow64 copy x86\libusb0_x86.dll %SystemRoot%\syswow64\libusb0.dll
devcon.exe rescan
rundll32 libusb0.dll,usb_install_driver_np_rundll usb_device.inf