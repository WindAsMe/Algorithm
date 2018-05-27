# !/usr/bin/python3
# -- coding: UTF-8 --
# Author   :WindAsMe
# Date     :18-5-13 下午4:47
# File     :paramTest.py
# Location:/Home/PycharmProjects/..


# like C value pass by reference
def list_add(a=[]):
    a.append('(')


# Python typical pass by value
def int_add(a):
    a += 1


# Python use return type
# Partial solve python problem that
# Can't pass by reference in int
def int_add_return(a):
    a += 1
    return a


if __name__ == '__main__':
    b = 0
    a = []
    # List pass by reference
    print('-----------------------------')
    print('list pass by reference')
    print(a)
    list_add(a)
    print(a)
    print('-----------------------------')
    print('-----------------------------')
    print('int pass by value')
    print(b)
    int_add(b)
    print(b)
    print('-----------------------------')
    print('-----------------------------')
    print('int pass by value and partial instead')
    print(b)
    b = int_add_return(b)
    print(b)
    print('-----------------------------')

