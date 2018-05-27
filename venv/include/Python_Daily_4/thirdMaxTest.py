# !/usr/bin/python3
# -- coding: UTF-8 --
# Author   :WindAsMe
# Date     :18-5-16 下午1:07
# File     :thirdMaxTest.py
# Location:/Home/PycharmProjects/..

# LeeCode No.414 BUT DIFFERENT
# Problem need data can be repeated


def thirdMax(nums=[]):
    """
    :type nums: List[int]
    :rtype: int
    """
    nums.sort()
    a = nums[-3:-2]
    if a == []:
        a = nums[len(nums) - 1]
    return a


if __name__ == '__main__':
    num = [1, 3, 4]
    print(thirdMax(num))
