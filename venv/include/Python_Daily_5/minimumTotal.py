# !/usr/bin/python3
# -- coding: UTF-8 --
# Author   :WindAsMe
# Date     :18-6-1 下午4:57
# File     :minimumTotal.py
# Location:/Home/PycharmProjects/..

# LeeCode No.120


class Solution:
    @staticmethod
    def minimumTotal(triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        if len(triangle) == 0:
            return 0
        elif len(triangle) == 1:
            return triangle[0][0]
        else:
            sum = []
            sum.append([triangle[0][0]])

            # From top to button
            # Dynamic programming
            for i in range(1, len(triangle)):
                temp = []
                for j in range(0, i+1):
                    if j == 0:
                        temp.append(sum[i - 1][0]+triangle[i][0])
                    elif j == i:
                        temp.append(sum[i - 1][j - 1] + triangle[i][j])
                    else:
                        temp.append(min(sum[i - 1][j - 1], sum[i - 1][j]) + triangle[i][j])
                sum.append(temp)
            return min(sum[len(sum) - 1])


if __name__ == '__main__':
    tip = [
            [2],
            [3,4],
            [6,5,7],
            [4,1,8,3]
                        ]
    print(Solution.minimumTotal(tip))