# !/usr/bin/python3
# -- coding: UTF-8 --
# Author   :WindAsMe
# Date     :18-5-31 下午9:38
# File     :singleNumber.py
# Location:/Home/PycharmProjects/..

# LeeCode No.137


class Solution:
    @staticmethod
    def singleNumber(nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        for i in range(0,len(nums)-3,3):
            if nums[i] == nums[i+1]:
                pass
            else:
                return nums[i]
        return nums[len(nums) - 1]

        # Only this is passed
        # set(): Transfer the nums to set, the elements is no repeat
        # sum(): Add all set value

        # return round((sum(set(nums))*3-sum(nums))/2)

if __name__ == '__main__':
    print(Solution.singleNumber([1,2,4,1,1,4,2,3,2,4]))
    a = [1,2,4,1,1,4,2,3,2,4]
    print((sum(set(a))*3-sum(a))/2)