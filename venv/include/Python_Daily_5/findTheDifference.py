# !/usr/bin/python3
# -- coding: UTF-8 --
# Author   :WindAsMe
# Date     :18-6-13 下午5:29
# File     :findTheDifference.py
# Location:/Home/PycharmProjects/..

# LeeCode No.389


class Solution:
    @staticmethod
    def findTheDifference(s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        if len(s) == 0:
            return t
        list1 = list(s)
        list1.sort()
        list2 = list(t)
        list2.sort()
        i = 0
        print(list1)
        print(list2)
        for i in range(len(list1)):
            if list1[i] != list2[i]:
                return list2[i]
        return list2[i+1]


if __name__ == '__main__':
    print(Solution.findTheDifference("", "abcde"))