# !/usr/bin/python3
# -- coding: UTF-8 --
# Author   :WindAsMe
# Date     :18-6-8 下午12:06
# File     :findKthLargest.py
# Location:/Home/PycharmProjects/..

# LeeCode No.215


class Solution:
    @staticmethod
    def findKthLargest(nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort()
        return nums[len(nums) - k]


if __name__ == '__main__':
    print(Solution.findKthLargest([3,4,5,1,2], 2))
