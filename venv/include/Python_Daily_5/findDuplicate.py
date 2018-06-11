# !/usr/bin/python3
# -- coding: UTF-8 --
# Author   :WindAsMe
# Date     :18-6-11 上午11:10
# File     :findDuplicate.py
# Location:/Home/PycharmProjects/..

# LeeCode No.287


class Solution:
    @staticmethod
    def findDuplicate(nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <= 1:
            return -1
        if nums.__len__() == set(nums).__len__():
            return -1
        return int((sum(nums) - sum(set(nums))) / (nums.__len__() - set(nums).__len__()))


if __name__ == '__main__':
    a = [1,1,1,2,3,4,5]
    print(Solution.findDuplicate(a))