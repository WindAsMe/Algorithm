# !/usr/bin/python3
# -- coding: UTF-8 --
# Author   :WindAsMe
# Date     :18-6-2 下午1:23
# File     :increasingTriplet.py
# Location:/Home/PycharmProjects/..

# LeeCode No.334


class Solution:
    @staticmethod
    def increasingTriplet(nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) <= 3:
            return False
        else:
            p1 = int("INF")
            p2 = int("INF")
            # Find the smaller and matched
            for i in range(0, len(nums)):
                if nums[i] <= p1:
                    p1 = nums[i]
                elif nums[i] <= p2:
                    p2 = nums[i]
                else:
                    return True
            return False


if __name__ == '__main__':
    print(Solution.increasingTriplet([2,1,5,0,4,6]))