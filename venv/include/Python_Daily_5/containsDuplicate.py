# !/usr/bin/python3
# -- coding: UTF-8 --
# Author   :WindAsMe
# Date     :18-6-6 下午2:22
# File     :containsDuplicate.py
# Location:/Home/PycharmProjects/..

# LeeCode No.217


class Solution:
    @staticmethod
    def containsDuplicate(nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        return len(set(nums)) != len(nums)


if __name__ == '__main__':
    print(Solution.containsDuplicate([1,2,3,1]))