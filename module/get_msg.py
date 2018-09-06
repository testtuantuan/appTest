# !/uer/bin/env python3
# coding=utf-8
from base.run_sql import GetData


class GetMsg:
    def __init__(self):
        self._msg = None

    @property
    def get_msg(self):
        return self._msg

    @get_msg.setter
    def get_msg(self, phone):
        if not isinstance(phone, str):
            raise TypeError("phone must be a str!")
        if len(phone) != 11:
            raise ValueError("非 11 位！")
        obj = GetData()
        msg = obj.get_result(
            "SELECT msg FROM czb_message.sms_log WHERE mobile={} GROUP BY send_time DESC LIMIT 1".format(phone))[0]
        self._msg = msg[4:8]


if __name__ == '__main__':
    run = GetMsg()
    run.get_msg = '13800138000'
    print(run.get_msg)
