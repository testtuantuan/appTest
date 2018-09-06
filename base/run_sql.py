# !/uer/bin/env python3
# coding=utf-8
import pymysql
import configparser
import re
from base.log import LOGGER, logged


class GetData:
    def __init__(self):
        self._conf = configparser.ConfigParser()
        self._conf.read('../conf.ini')
        self._db = None
        self._cursor = None

    def _connect_db(self):
        _server_conf = {'host': self._conf.get("SERVER", "host"),
                        'user': self._conf.get("SERVER", "username"),
                        'passwd': self._conf.get("SERVER", "password"),
                        'port': int(self._conf.get("SERVER", "port")),
                        'charset': self._conf.get("SERVER", "charset")}
        try:
            self._db = pymysql.connect(**_server_conf)
            self._cursor = self._db.cursor()
            LOGGER.info("数据库连接成功！")
        except ConnectionError as ex:
            LOGGER.error(str(ex))

    @logged
    def get_result(self, sql):
        self._connect_db()
        try:
            self._cursor.execute(sql)
            self._db.commit()
            result = self._cursor.fetchone()
            return result
        except Exception as e:
            LOGGER.error("执行语句出错了。错误信息：{}".format(e))
        finally:
            self.close_db()

    @logged
    def close_db(self):
        self._db.close()
        LOGGER.info("数据库连接关闭！")

    @logged
    def get_msg(self, phone):
        result = self.get_result(
            "SELECT msg FROM czb_message.sms_log WHERE mobile={} GROUP BY send_time DESC LIMIT 1".format(phone))
        file = re.compile("验证码：\d{4}", re.S)
        j = re.findall(file, result[0])
        msg_code = j[0][-4:]
        return msg_code


if __name__ == '__main__':
    run = GetData()
    c = run.get_msg()
    print(c)
