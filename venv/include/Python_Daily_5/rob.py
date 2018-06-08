# !/usr/bin/python3
# -- coding: UTF-8 --
# Author   :WindAsMe
# Date     :18-6-8 下午1:47
# File     :rob.py
# Location:/Home/PycharmProjects/..

# LeeCode No.213


class Solution:
    def __init__(self):
        self.nums_dict = {}

    def rob0(self, house_lists, head):
        if len(house_lists) > 3:
            index = 0
            sum_now = 0
            while index < 2:
                if head + index + 2 not in self.nums_dict.keys():
                    self.nums_dict[head + index + 2] = self.rob0(house_lists[index + 2:], head + index + 2)
                sum_temp = self.nums_dict[head + index + 2] + house_lists[index]
                if sum_temp > sum_now:
                    sum_now = sum_temp
                index += 1
            return sum_now
        if len(house_lists) == 1:
            return house_lists[0]
        if len(house_lists) == 2:
            if house_lists[0] > house_lists[1]:
                return house_lists[0]
            return house_lists[1]
        if len(house_lists) == 3:
            if house_lists[0] + house_lists[2] > house_lists[1]:
                return house_lists[0] + house_lists[2]
            return house_lists[1]

    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        sum1 = self.rob0(nums[0:len(nums) - 1], 0)
        self.nums_dict = {}
        sum2 = self.rob0(nums[1:], 1)
        if sum1 > sum2:
            return sum1
        return sum2


if __name__ == '__main__':
    a = Solution()

    print(a.rob([29,83,62,52,7,44,33,11,88,5,3,21,12]))