# !/usr/bin/python3
# -- coding: UTF-8 --
# Author   :WindAsMe
# Date     :18-5-13 下午4:47
# File     :serverTest.py
# Location:/Home/PycharmProjects/..

import socket


if __name__ == 'main':
    s = socket.socket()
    host = socket.gethostname()
    port = 12345
    s.bind((host, port))

    # Listening and waiting
    s.listen(5)
    while True:
        # Create connection with client
        c, addr = s.accept()
        print('连接地址：', addr)
        c.send('欢迎访问菜鸟教程！')
        # Close
        c.close()
