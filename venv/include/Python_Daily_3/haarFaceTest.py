# !/usr/bin/python3
# -- coding: UTF-8 --
# Author   :WindAsMe
# Date     :18-5-13 下午4:47
# File     :haarFaceTest.py
# Location:/Home/PycharmProjects/..

import matplotlib.pyplot as p
import matplotlib.image as m
import numpy as np


if __name__ == '__main__':
    pic = m.imread('us.png')
    p.imshow(pic)
    p.show()
