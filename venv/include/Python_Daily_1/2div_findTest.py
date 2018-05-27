# !/usr/bin/python3
# -- coding: UTF-8 --
# Author   :WindAsMe
# Date     :18-5-13 下午4:47
# File     :2div_findTest.py
# Location:/Home/PycharmProjects/..

import math


# Binary Chop
# In Iterator
def div_find(s, need, start, end):
    # Round down
    mid = math.floor((start + end)/2)
    if need == s[mid]:
        print("need find out !", " value: ", need, " index: ", mid)
    elif need > s[mid]:
        div_find(s, need, mid, end)
    else:
        div_find(s, need, start, mid)


# Eight Queue
# Solving conflict
def conflict(i, x, y):
    # a = [(0, 1), (1, 1), (4, 2)]
    # print(a[0][0])
    """
    find conflict is exist or not
    :param i: list like a
    :param x: nextX
    :param y: nextY
    :return:is has conflict
    """
    for index in i:
        if x == index[0] or y == index[1]:
            return False
        elif abs(x-index(0)) == abs(y-index(1)):
            return False
    return True


def eight_queen(num=8, i=[]):

    """
    find eight queen
    :param num: scale of queen
    :param i: already set queen position
    :return:
    """
    for posX in range(num):
        for posY in range(num):
            if not conflict(i, posX, posY):
                if len(i) == num-1:
                    i.append((posX, posY))
                    return i
                else:
                    i.append((posX, posY))


if __name__ == '__main__':
    i = []
    print(eight_queen(8, i))

