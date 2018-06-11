# !/usr/bin/python3
# -- coding: UTF-8 --
# Author   :WindAsMe
# Date     :18-6-8 下午5:10
# File     :addDigits.py
# Location:/Home/PycharmProjects/..

# LeeCode No.258


class Solution:
    @staticmethod
    def addDigits(num):
        """
        :type num: int
        :rtype: int
        """
        num1 = 0
        while not ((num == 0 and num1 < 10) or (num1 == 0 and num < 10)):
            if num1 == 0:
                while num != 0:
                    num1 += int(num % 10)
                    num = int(num / 10)
            if num == 0:
                while num1 != 0:
                    num += int(num1 % 10)
                    num1 = int(num1 / 10)
        return max(num, num1)


if __name__ == '__main__':
    print(Solution.addDigits(38))