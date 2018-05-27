# !/usr/bin/python3
# -- coding: UTF-8 --
# Author   :WindAsMe
# Date     :18-5-13 下午4:47
# File     :smtpTestTest.py
# Location:/Home/PycharmProjects/..

import smtplib
from email.mime.text import MIMEText
from email.header import Header


if __name__ == '__main__':
    sender = 'from@runoob.com'
    # Receiver's email
    receivers = ['542636539@qq.com']

    # Three Params：
    # 1.Content of message
    # 2.Content format
    # 3.Set utf-8 code
    message = MIMEText('Python 邮件发送测试...', 'plain', 'utf-8')
    # Sender
    message['From'] = Header("菜鸟教程", 'utf-8')
    # Receiver
    message['To'] = Header("测试", 'utf-8')

    subject = 'Python SMTP 邮件测试'
    message['Subject'] = Header(subject, 'utf-8')

    try:
        smtpObj = smtplib.SMTP('localhost')
        smtpObj.sendmail(sender, receivers, message.as_string())
        print("邮件发送成功")
    except smtplib.SMTPException:
        print("Error: 无法发送邮件")
