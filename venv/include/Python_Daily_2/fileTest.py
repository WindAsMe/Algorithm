# !/usr/bin/python3
# -- coding: UTF-8 --
# Author   :WindAsMe
# Date     :18-5-13 下午4:47
# File     :fileTest.py
# Location:/Home/PycharmProjects/..

import sys
import pprint

if __name__ == '__main__':
    # A file-open object

    # Read(including readline readlines)
    # All read function read the next unread
    f = open('file.txt', 'r+')
    try:
        # Simple read
        print('file read:', f.read(5))

        # Readline
        # Read one row
        print('file readline:', f.readline())

        # Readlines
        # One row as a String
        # All combine a list
        print('file readlines:', f.readlines())

        # Write data
        # Use '\n' can change row
        s = '\nC is difficult'
        f.write(s)
    finally:
        f.close()
