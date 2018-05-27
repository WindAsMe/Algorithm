# !/usr/bin/python3
# -- coding: UTF-8 --
# Author   :WindAsMe
# Date     :18-5-13 下午4:47
# File     :heapTest.py
# Location:/Home/PycharmProjects/..

from heapq import *
import random

if __name__ == '__main__':
    # Data = [1, 2, 3, 4....]
    data = list(range(10))
    # Make data[] random
    random.shuffle(data)
    heap = []
    print(data)
    for n in data:
        # Create small root heap
        heappush(heap, n)
    print(heap)
    # Rebuilt heap
    # Make it into small root heap
    heappush(heap, 0.5)
    print(heap)
    # Pop the root
    # Pop the smallest one
    print(heappop(heap))
    # Continue heappop
    print(heappop(heap))
    # After heappop
    print(heap)

    # Combine the heappop and heappush
    # More efficient
    heapreplace(heap, 0)
    print(heap)

    # Find the nlargest data in  Iteration
    # Familiar with the FUNCTION:
    # 1. list.sorted()
    # 2. list[0:] AO
    # BUT MORE EFFICIENT
    print(nlargest(2, heap))

    print(nsmallest(2, heap))