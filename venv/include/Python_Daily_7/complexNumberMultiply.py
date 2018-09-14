# !/usr/bin/python3
# -- coding: UTF-8 --
# Author   :WindAsMe
# Date     :18-9-14 下午1:53
# File     :complexNumberMultiply.py
# Location:/Home/PycharmProjects/..

# LeetCode No.537

class Solution:
    @staticmethod
    def complexNumberMultiply(a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        real1 = a.split('+')
        real2 = b.split('+')
        virtual1 = real1[1].split('i')
        virtual2 = real2[1].split('i')
        real = int (real1[0]) * int (real2[0]) - int (virtual1[0]) * int (virtual2[0])
        virtual = int (real1[0]) * int (virtual2[0]) + int (real2[0]) * int (virtual1[0])
        return "%d+%di" % (real, virtual)

if __name__ == '__main__':
    print(Solution.complexNumberMultiply("1+1i", "1+-1i"))