# !/usr/bin/python3
# -- coding: UTF-8 --
# Author   :WindAsMe
# Date     :18-5-13 下午4:47
# File     :modelTest.py
# Location:/Home/PycharmProjects/..


class Person:

    # Construct
    def __init__(self):
        self.__name = 0

    def __plus__(self):
        self.__name += 1

    def __print__(self):
        print('name:', self.__name)


class People:
    # Like Java static member
    # All object support it
    name = 0

    @staticmethod
    def init():
        People.name += 1

    @staticmethod
    def out():
        print('name:', People.name)


if __name__ == "__main__":
    a = Person()
    a.__plus__()
    a.__print__()

    b = Person()
    b.__plus__()
    b.__print__()

    c = People()
    c.init()
    c.out()

    d = People()
    d.init()
    d.out()
