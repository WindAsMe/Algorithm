# !/usr/bin/python3
# -- coding: UTF-8 --
# Author   :WindAsMe
# Date     :18-6-8 下午3:19
# File     :summaryRanges.py
# Location:/Home/PycharmProjects/..

# LeeCode No.228


class Solution:
    @staticmethod
    def summaryRanges(nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        if len(nums) == 0:
            return nums
        elif len(nums) == 1:
            return [str(nums[0])]
        elif len(nums) == 2:
            if nums[0] + 1 == nums[1]:
                tip = str(nums[0]).__add__("->").__add__(str(nums[1]))
                return [tip]
            else:
                return [str(nums[0]), str(nums[1])]
        else:
            result = []
            start = nums[0]
            end = nums[0]
            for i in range(1, len(nums)):
                print('start: ', start, ' end: ', end, ' value: ', nums[i])
                if nums[i] - nums[i - 1] == 1:
                    end = nums[i]
                else:
                    if start == end:
                        result.append(str(start))
                        start = nums[i]
                        end = nums[i]
                    else:
                        result.append(str(start).__add__("->").__add__(str(end)))
                        start = nums[i]
                        end = nums[i]
            if start == end:
                result.append(str(start))
            else:
                result.append(str(start).__add__("->").__add__(str(end)))
            return result




if __name__ == '__main__':

    print(Solution.summaryRanges([1, 2]))

