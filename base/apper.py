# !/uer/bin/env python3
# coding=utf-8
from appium import webdriver
from .device_msg import DevicesMassage
from .conf_writer import write_conf


def Apper():
    platform = write_conf()
    _url = DevicesMassage().get_url()

    if platform == 'android':
        # 取安卓设备信息
        _devices_msg = DevicesMassage().get_android_msg()
        return webdriver.Remote(_url, _devices_msg)
    if platform == 'ios':
        # 取ios设备信息
        _devices_msg = DevicesMassage().get_ios_msg()
        return webdriver.Remote(_url, _devices_msg)
    if platform == 'simulator':
        # 取模拟器信息
        _devices_msg = DevicesMassage().get_ios_simulator_msg()
        return webdriver.Remote(_url, _devices_msg)
