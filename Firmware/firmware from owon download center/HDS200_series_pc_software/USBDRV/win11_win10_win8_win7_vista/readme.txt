make sure the usb device is connected and working:
run reinstall.bat  to remove all versions of usb drivers and automatically install the new version of usb driver.
for advance using:
run uninstall.bat to remove all versions of usb drivers.

ȷ������ʱ�豸��������PC�����ڿ���״̬��
����reinstall.bat��ж�����а汾�����������Զ���װ�µ�������
���ⱸ�ã�
����uninstall.bat��ж�����а汾��������

��װ:
devcon.exe update usb_device.inf "usb\vid_5345&pid_1234"
rundll32 libusb0.dll,usb_install_driver_np_rundll usb_device.inf