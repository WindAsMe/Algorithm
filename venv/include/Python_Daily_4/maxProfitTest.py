# !/usr/bin/python3
# -- coding: UTF-8 --
# Author   :WindAsMe
# Date     :18-5-14 下午4:14
# File     :maxProfitTest.py
# Location:/Home/PycharmProjects/..

# LeeCode No.122


class Solution:
    @staticmethod
    def max_profit(prices):
        if len(prices) <= 1:
            return 0
        n = len(prices)
        sum_value = 0
        max_value = 0
        for i in range(1, n):
            sum_value = max(0, prices[i]-prices[i-1])
            max_value += sum_value
        return max_value


if __name__ == '__main__':
    print(Solution.max_profit([7, 1, 5, 3, 6, 4]))
