# device is the cyanogenmod codename for the device
# eg mako is Nexus 4
%define device find5
# vendor is used in device/oppo/find5/
%define vendor oppo
# Manufacrurer and device name to be shown in UI
%define vendor_pretty OPPO
%define device_pretty Find 5

%define android_config \
#define QCOM_BSP 1\
%{nil}

%include rpm/droid-hal-device.inc
