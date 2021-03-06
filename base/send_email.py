# !/uer/bin/env python3
# coding=utf-8

import smtplib
import configparser
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.utils import formataddr
from base.log import logged, LOGGER

conf = configparser.ConfigParser()
conf.read("../conf.ini")


class SendEmail(object):
    def __init__(self):
        self._mail_host = conf.get("EMAIL", "mail_host")
        self._rec_user = conf.get("EMAIL", "rec_user")
        self._mail_pass = conf.get("EMAIL", "mail_pass")
        self._sender = conf.get("EMAIL", "sender")
        self._message = MIMEMultipart()
        self._message['From'] = formataddr(["Python3", self._sender])
        self._message['To'] = formataddr(["Me", self._rec_user])
        self._message['Subject'] = "**** 自动化测试报告 ****"

    @logged
    def send_text_to_email(self, msg):
        """
        发送纯文本格式邮件
        warning: 这个方法不能与发送html方法共用，如果共用以先执行的方法发送，后执行的方法无效
        :param msg:  type(str)
        """
        self._message.attach(MIMEText(msg, 'plain'))
        self._send_email()

    @logged
    def send_html_to_email(self, fp):
        """
        发送html格式邮件
        :param fp: 要发送文件的绝对路径或相对路径
        :return:
        """
        with open(fp, 'r', encoding='utf-8') as f:
            page_source = f.read()
            self._message.attach(MIMEText(page_source, 'html'))
        self._send_email()

    @logged
    def send_file_to_email(self, fp):
        """
        发送附件格式邮件
        :param fp: 要发送文件的绝对路径或相对路径
        :return:
        """
        att = MIMEText(open(fp, 'rb').read(), 'base64', 'utf-8')
        att["Content-Type"] = 'application/octet-stream'
        att["Content-Disposition"] = 'attachment; filename="log.txt'
        self._message.attach(att)
        self._send_email()

    @logged
    def _send_email(self):
        try:
            smtp_obj = smtplib.SMTP(self._mail_host, 25)
            smtp_obj.login(self._sender, self._mail_pass)
            smtp_obj.sendmail(self._sender, [self._rec_user, ], self._message.as_string())
            LOGGER.info("邮件发送成功")
            smtp_obj.quit()
        except smtplib.SMTPException as e:
            LOGGER.error("Error: 无法发送邮件, {}".format(e))
            raise e


if __name__ == '__main__':
    run = SendEmail()
    run.send_html_to_email("../case/report/2018-07-04_17_38_52result.html")
    print("html 发送成功!")
    run.send_text_to_email("这是一个神奇的代码！！！")
    print("text 发送成功!")
    run.send_file_to_email("../case/logs/2018-07-04_17_23_40.log")
    print("file 发送成功!")
