# !/usr/bin/python3
# -- coding: UTF-8 --
# Author   :WindAsMe
# Date     :18-5-13 下午4:47
# File     :iteratorTest.py
# Location:/Home/PycharmProjects/..


class TestIterator:
    value = 0

    # __next__ return iterator.next element
    def __next__(self):
        self.value += 1
        if self.value > 10:
            raise StopIteration
        return self.value

    # __iter__ return iterator object
    def __iter__(self):
        return self


if __name__ == '__main__':
    test = TestIterator()
    a = []
    try:
        while True:
            a.append(test.__next__())
    except StopIteration:
        pass
    print(a)
