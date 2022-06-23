make sure the usb device is connected and working:
run reinstall.bat  to remove all versions of usb drivers and automatically install the new version of usb driver.
for advance using:
run uninstall.bat to remove all versions of usb drivers.

确保运行时设备已连接上PC并处于开启状态：
运行reinstall.bat来卸载所有版本的驱动，并自动安装新的驱动。
额外备用：
运行uninstall.bat来卸载所有版本的驱动。

安装:
devcon.exe update usb_device.inf "usb\vid_5345&pid_1234"
rundll32 libusb0.dll,usb_install_driver_np_rundll usb_device.inf