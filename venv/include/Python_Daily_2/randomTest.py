# !/usr/bin/python3
# -- coding: UTF-8 --
# Author   :WindAsMe
# Date     :18-5-13 下午4:47
# File     :randomTest.py
# Location:/Home/PycharmProjects/..

import random as r

if __name__ == '__main__':
    # Return read number
    # Range from 0 to 1
    print(r.random())

    # Return read number
    # Range from param1 to param2 (including)
    print(r.uniform(10, 100))

    # Rebuild the list
    # All tuple occur have same possibility
    # Tuple is UNCHANGEABLE
    a = [(1, 2), (3, 4), (5, 6), (7, 8, 9)]
    r.shuffle(a)
    print(a)

    # Random choice the tuple / element from list
    b = r.choice(a)
    print(b)

    # Random choice the number of n tuples / elements from list
    # Function like random.choice()
    print(r.sample(a, 2))
