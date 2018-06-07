# !/usr/bin/python3
# -- coding: UTF-8 --
# Author   :WindAsMe
# Date     :18-6-7 下午8:05
# File     :MyQueue.py
# Location:/Home/PycharmProjects/..

# LeeCode No.232


class MyQueue:

    _innerList = []
    def __init__(self):
        """
        Initialize your data structure here.
        """

    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: void
        """
        self._innerList.append(x)

    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        temp = self._innerList[0]
        del self._innerList[0]
        return temp

    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        return self._innerList[0]

    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        return self._innerList == []

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()