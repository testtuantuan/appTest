# !/uer/bin/env python3
# coding=utf-8
import configparser
import os
from base.log import logged


class DevicesMassage:
    def __init__(self):
        self._conf = configparser.ConfigParser()
        self._conf.read('../conf.ini')
        self._devices_msg = {}
        self._url = None
        self.app_path = None

    @logged
    def get_url(self):
        self._url = self._conf.get('BASE', 'url')
        return self._url

    @logged
    def get_android_msg(self):
        self.app_path = os.path.join(os.path.dirname(__file__), self._conf.get('ANDROID', 'app'))
        self._devices_msg = {'platformName': self._conf.get('ANDROID', 'platformName'),
                             'deviceName': self._conf.get('ANDROID', 'deviceName'),
                             'platformVersion': self._conf.get('ANDROID', 'platformVersion'),
                             'appPackage': self._conf.get('ANDROID', 'appPackage'),
                             'appActivity': self._conf.get('ANDROID', 'appActivity'),
                             'unicodeKeyboard': self._conf.get('ANDROID', 'unicodeKeyboard'),
                             'resetKeyboard': self._conf.get('ANDROID', 'resetKeyboard'),
                             'app': self.app_path}
        return self._devices_msg

    @logged
    def get_ios_msg(self):
        self.app_path = os.path.join(os.path.dirname(__file__), self._conf.get('IOS', 'app'))
        self._devices_msg = {'platformName': self._conf.get('IOS', 'platformName'),
                             'deviceName': self._conf.get('IOS', 'deviceName'),
                             'platformVersion': self._conf.get('IOS', 'platformVersion'),
                             'bundleId': self._conf.get('IOS', 'bundleId'),
                             'udid': self._conf.get('IOS', 'udid'),
                             'automationName': self._conf.get('IOS', 'automationName'),
                             'app': self.app_path + '.ipa',
                             'xcodeOrgId': self._conf.get('IOS', 'xcodeOrgId'),
                             'xcodeSigningId': self._conf.get('IOS', 'xcodeSigningId'),
                             'autoAcceptAlerts': 'true',
                             'waitForAppScript': 'true'}
        return self._devices_msg

    @logged
    def get_ios_simulator_msg(self):
        self.app_path = os.path.join(os.path.dirname(__file__), self._conf.get('IOS', 'app'))
        self._devices_msg = {'app': self.app_path + '.app',
                             'platformName': self._conf.get('IOS', 'platformName'),
                             'platformVersion': self._conf.get('IOS', 'platformVersion'),
                             'deviceName': self._conf.get('IOS', 'deviceName'),
                             'bundleId': self._conf.get('IOS', 'bundleId'),
                             'uuid': self._conf.get('IOS', 'uuid'),
                             'autoAcceptAlerts': 'true',
                             'waitForAppScript': 'true'}
        return self._devices_msg
