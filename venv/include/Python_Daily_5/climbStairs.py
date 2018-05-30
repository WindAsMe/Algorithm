# !/usr/bin/python3
# -- coding: UTF-8 --
# Author   :WindAsMe
# Date     :18-5-30 下午8:48
# File     :climbStairs.py
# Location:/Home/PycharmProjects/..

# LeeCode No.70


class Solution:
    @staticmethod
    def climbStairs(n):
        """
        :type n: int
        :rtype: int
        """
        step = 0
        if n == 1:
            step += 1
            return step
        elif n == 2:
            step += 2
            return step
        else:
            step += Solution.climbStairs(n-1)
            step += Solution.climbStairs(n-2)
            return step


if __name__ == '__main__':
    print(Solution.climbStairs(35))