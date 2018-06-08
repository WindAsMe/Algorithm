# !/usr/bin/python3
# -- coding: UTF-8 --
# Author   :WindAsMe
# Date     :18-6-8 下午12:16
# File     :heapqTest.py
# Location:/Home/PycharmProjects/..

# heapq package test

import heapq
import random

if __name__ == '__main__':
    heap = []
    data = random.sample(range(1, 8), 7)
    print('data: ', data)

    for i in data:
        heapq.heappush(heap, i)