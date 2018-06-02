# !/usr/bin/python3
# -- coding: UTF-8 --
# Author   :WindAsMe
# Date     :18-6-2 下午6:03
# File     :findMin.py
# Location:/Home/PycharmProjects/..

# LeeCode No.153


class Solution:

    @staticmethod
    def findMin(nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return
        elif len(nums) == 1:
            return nums[0]
        else:
            temp = nums[0]
            for i in range(len(nums) - 1):
                if nums[i] > nums[i + 1]:
                    temp = nums[i + 1]
                    break
            return temp


if __name__ == '__main__':
    print(Solution.findMin([4,5,6,7,0,1,2]))