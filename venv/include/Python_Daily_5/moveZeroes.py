# !/usr/bin/python3
# -- coding: UTF-8 --
# Author   :WindAsMe
# Date     :18-6-6 下午9:12
# File     :moveZeroes.py
# Location:/Home/PycharmProjects/..

# LeeCode No.283


class Solution:
    @staticmethod
    def moveZeroes(nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if 0 in nums:
            len1 = len(nums)
            nums.remove(0)
            len2 = len(nums)
            nums.sort()
            # print('len1:', len1, ' len2:', len2)
            while len2 != len1:
                nums.append(0)
                len2 += 1
            return nums
        else:
            nums.sort()
            return nums


if __name__ == '__main__':
    print(Solution.moveZeroes([1,2,4,8,4]))