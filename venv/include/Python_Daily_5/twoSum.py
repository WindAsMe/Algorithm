# !/usr/bin/python3
# -- coding: UTF-8 --
# Author   :WindAsMe
# Date     :18-6-2 下午6:29
# File     :twoSum.py
# Location:/Home/PycharmProjects/..

# LeeCode No.167


class Solution:

    @staticmethod
    def twoSum(numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        result =[]
        begin = 0
        end = len(numbers) - 1
        while numbers[begin] + numbers[end] != target:
            if numbers[begin] + numbers[end] > target:
                end -= 1
            else:
                begin += 1
        result.append(begin + 1)
        result.append(end + 1)
        return result


if __name__ == '__main__':
    print(Solution.twoSum([2, 7, 11, 15], 9))