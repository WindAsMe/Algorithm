# !/usr/bin/python3
# -- coding: UTF-8 --
# Author   :WindAsMe
# Date     :18-5-14 下午4:48
# File     :barChartTest.py
# Location:/Home/PycharmProjects/..

# LeeCode No.84


class Solution:
    @staticmethod
    def largest_rectangle_area(heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        if len(heights) == 0:
            return 0
        elif len(heights) == 1:
            return heights[0]
        else:
            # Saving max height
            height_max = 0
            # Saving max area
            area_max = 0
            for element in range(len(heights)):
                if heights[element] >= height_max:
                    height_max = heights[element]

            # Get height == temp
            # Longest index
            # Max_area = longest_index * height
            longest_index = 0
            temp_longest_index = 0
            for height in range(1, height_max+1):
                # Iterate list
                for index in range(0, len(heights)):
                    if heights[index] >= height:
                        temp_longest_index += 1
                        longest_index = max(longest_index, temp_longest_index)
                    else:
                        temp_longest_index = 0
                # Compare different height's area
                # Carry the biggest
                area_max = max(area_max, height*longest_index)
                # Both int clear
                print('index', longest_index)
                temp_longest_index = 0
                longest_index = 0
            return area_max


if __name__ == '__main__':
    print(Solution.largest_rectangle_area([2, 0, 2]))

