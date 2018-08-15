# !/usr/bin/python3
# -- coding: UTF-8 --
# Author   :WindAsMe
# Date     :18-8-14 下午8:48
# File     :wavToPcm.py
# Location:/Home/PycharmProjects/..
import os
import numpy as np


if __name__ == '__main__':
    f = open("test.wav")
    f.seek(0)
    f.read(44)
    data = np.fromfile(f, dtype=np.int16)
    data.tofile("test.pcm")