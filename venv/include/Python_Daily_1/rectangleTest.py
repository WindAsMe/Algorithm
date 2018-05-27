# !/usr/bin/python3
# -- coding: UTF-8 --
# Author   :WindAsMe
# Date     :18-5-13 下午4:47
# File     :rectangleTest.py
# Location:/Home/PycharmProjects/..


def judge(i):
    if not isinstance(i, tuple):
        raise TypeError


class Rectangle:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    @property
    def size(self):
        return self._length, self._width

    @size.setter
    def length(self, value):
        self._length = value

    @size.setter
    def width(self, value):
        self._width = value


if __name__ == '__main__':
    r = Rectangle(1, 2)
    r.length = 4
    r.width = 11
    print(r.size)
