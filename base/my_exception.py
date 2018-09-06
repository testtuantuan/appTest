# !/uer/bin/env python3
# coding=utf-8
from base.log import logged


class MyException(Exception):
    @logged
    def __init__(self, msg):
        super().__init__(self)
        self.msg = msg

    @logged
    def __str__(self):
        return self.msg
