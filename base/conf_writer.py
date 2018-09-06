# !/uer/bin/env python3
# coding=utf-8
import subprocess
import configparser
import os
import re
from base.log import LOGGER, logged


@logged
def _get_android_devices_list():
    """
    取连接设备的devices name，支持多设备
    :return: list 返回一个设备列表
    """
    res = _send_command('adb devices')
    if not res:
        LOGGER.info("设备未开启开发者模式中的adb调试！{}".format(res))
    devices_name = res.decode('utf-8').split('\n')[1:-2]
    devices_list = [i.split('\t')[0] for i in devices_name]
    return devices_list


@logged
def _get_android_platform_version():
    """
    取连接设备的android系统版本，仅支持单设备
    :return: str
    """
    res = _send_command('adb shell getprop ro.build.version.release')
    if not res:
        LOGGER.warning("未取到系统版本！！！{}".format(res))
    return res.decode('utf-8').strip('\r\n')


@logged
def _get_ios_device():
    """获取ios设备信息, 不支持多设备"""
    u = _send_command('idevice_id -l')
    if u:
        udid = (str(u)[2:-3])
        if udid:
            b_device_name = _send_command('idevicename -u {}'.format(str(udid)))
            device_name = (str(b_device_name)[2:-3])
            b_device_version = _send_command('ideviceinfo -u {} -k ProductVersion'.format(udid))
            device_version = (str(b_device_version)[2:-5])  # 这里的取值需要视自己mac里的sdk版本而定
            return udid, device_name, device_version
    else:
        return None, None, None


@logged
def _get_bundle_id(package_file='../package_test/'):
    """
    获取ios设备的bundleID,不支持多设备
    :param package_file: app的文件路径
    :return: bundle id (string)
    """
    path = os.path.join(os.getcwd(), package_file)
    all_file = (os.listdir(path))
    for f in all_file:
        file = re.compile(".*.ipa", re.S)
        j = re.findall(file, f)
        if len(j) > 1:
            raise FileExistsError("{}文件夹下发现多个ipa文件！请确认只存在一个".format(package_file))
        if len(j) == 1:
            file_path = os.path.join(path, j[0])
            app = j[0].split('.')[0] + '.app'
            res_byte = _send_command(
                'unzip -oq {} && cd Payload/{} && defaults read `pwd`/Info CFBundleIdentifier'.format(file_path, app))
            bundle_id = str(res_byte)[2:-3]
            return bundle_id


@logged
def _get_ios_simulator_conf(device):
    """
    获取mac os 设备上的手机模拟器信息
    :param device: 要获取的设备名称，如iPhone 7 或 iPhone 7 Plus
    :return:
    """
    simulator_devices = _send_command("instruments -s devices")
    devices = re.compile(device + '.*', re.S)
    res = re.findall(devices, str(simulator_devices))
    simulators = res[0].split("\\n")
    sdk = _send_command("xcodebuild -showsdks")
    simulator_sdk_version = str(sdk).split('\\n\\n')[1].split('\\n\\t')[1].split('\\t')[0].split(' ')[3]
    re1 = re.compile('\(' + simulator_sdk_version + '.*', re.S)
    one_simulator = re.findall(re1, str(simulators))[0].split("\'")[0]
    uuid_re = re.compile("\[.*]", re.S)
    uuid = re.findall(uuid_re, one_simulator)[0][1:-1]
    return device, simulator_sdk_version, uuid


@logged
def _send_command(command):
    """通过管道发送命令"""
    try:
        res = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE)
        res.wait()
        result = res.stdout.read()
    except subprocess.CalledProcessError as e:
        LOGGER.warning("命令运行失败！{}".format(e))
        raise
    return result


@logged
def write_conf(device_re="iPhone 7 Plus"):
    """
    把上面取到的设备信息写入到conf.ini文件中
    :param device_re: 运行设备名称
    :return:
    """
    conf = configparser.ConfigParser()
    conf.read("../conf.ini")
    device_name = _get_android_devices_list()
    if device_name:
        platform_version = str(_get_android_platform_version())
        conf.set("ANDROID", "platformVersion", platform_version)
        conf.set("ANDROID", "deviceName", device_name[0])
        conf.write(open("../conf.ini", "w"))
        LOGGER.info("写入配置文件成功，参数为platformVersion:{},deviceName:{}".format(platform_version, device_name))
        return 'android'
    else:
        udid, device_name, device_version = _get_ios_device()
        if udid:
            bundle_id = _get_bundle_id()
            conf.set("IOS", "udid", udid)
            conf.set("IOS", "deviceName", device_name)
            conf.set("IOS", "platformVersion", device_version)
            conf.set("IOS", "bundleId", bundle_id)
            conf.write(open("../conf.ini", "w"))
            LOGGER.info("写入配置文件成功，参数为deviceName:{},platformVersion:{},bundleId:{},udid:{}"
                        .format(device_name, device_version, bundle_id, udid))
            return 'ios'
        else:
            platform_name, platform_version, uuid = _get_ios_simulator_conf(device_re)
            bundle_id = _get_bundle_id()
            conf.set("IOS", "uuid", uuid)
            conf.set("IOS", "deviceName", platform_name)
            conf.set("IOS", "platformVersion", platform_version)
            conf.set("IOS", "bundleId", bundle_id)
            conf.write(open("../conf.ini", "w"))
            LOGGER.info("写入配置文件成功，参数为platform_name:{},platform_version:{},bundleId{},uuid:{}"
                        .format(platform_name, platform_version, bundle_id, uuid))
            return 'simulator'
