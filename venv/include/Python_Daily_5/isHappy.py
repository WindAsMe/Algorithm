# !/usr/bin/python3
# -- coding: UTF-8 --
# Author   :WindAsMe
# Date     :18-6-1 下午9:38
# File     :isHappy.py
# Location:/Home/PycharmProjects/..

# LeeCode No.202


class Solution:

    @staticmethod
    def isHappy(n):
        """
        :type n: int
        :rtype: bool
        """
        sum = n
        while(True):
            sum = numSum(sum)
            print(sum)
            if sum == 4:
                break
            if sum == 1:
                return True

        return False;


def numSum(n):
    sum = 0
    while n != 0:
        x = n % 10
        n = int(n / 10)
        sum += x * x
    return sum


if __name__ == '__main__':
    print(Solution.isHappy(1))
