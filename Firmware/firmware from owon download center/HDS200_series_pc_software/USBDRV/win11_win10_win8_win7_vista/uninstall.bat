devcon.exe rescan
devcon.exe remove "usb\vid_5345&pid_1234"
del %SystemRoot%\system32\drivers\Oscilloscopeusb.sys
del %SystemRoot%\system32\drivers\owonhdsusb.sys
del %SystemRoot%\inf\owonhdsusb.Inf
del %SystemRoot%\inf\owonhdsusb.PNF
del %SystemRoot%\system32\drivers\libusb0.sys
del %SystemRoot%\system32\libusb0.dll