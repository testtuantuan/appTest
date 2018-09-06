# !/uer/bin/env python3
# coding=utf-8
import datetime
import logging
import functools
import os
import traceback
import inspect

if "logs" in os.listdir('../'):
    pass
else:
    os.mkdir('../logs')
now = datetime.datetime.now().strftime('%Y-%m-%d_%H_%M_%S')
_log_fp = "../logs/" + now + ".log"
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                    datefmt='%a, %d %b %Y %H:%M:%S',
                    filename=_log_fp,
                    filemode='w')

_console = logging.StreamHandler()
_console.setLevel(logging.INFO)
formatter = logging.Formatter('%(name)-12s: %(levelname)-8s %(message)s')
_console.setFormatter(formatter)
LOGGER = logging.getLogger('czb test')
LOGGER.addHandler(_console)


def logged(method):
    """创建一个日志装饰器，它会记录所装饰函数的入参和
    这是一个很糟糕的代码，需要把logging模块替换为CLog
    """
    return_value = None

    @functools.wraps(method)
    def inner(*args, **kwargs):
        start = datetime.datetime.now()

        try:
            nonlocal return_value
            return_value = method(*args, **kwargs)
        except Exception:
            e = traceback.format_exc()
            LOGGER.error('Exception：{}'.format(e))
        finally:
            pass

        end = datetime.datetime.now()
        delta = end - start

        LOGGER.info('调用 {}函数；\n 传入参数: {}\n 或许还有: {},\n 返回结果: {} ;\n'
                    .format(inspect.stack()[1][3], str(args), str(kwargs), return_value))
        LOGGER.warning('调用 {}函数；\n 时间 {};\n 执行时间 {} ;\n'
                       .format(inspect.stack()[1][3], start, delta, return_value))

        return return_value

    return inner
