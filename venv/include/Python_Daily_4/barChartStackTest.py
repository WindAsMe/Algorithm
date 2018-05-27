# !/usr/bin/python3
# -- coding: UTF-8 --
# Author   :WindAsMe
# Date     :18-5-14 下午7:09
# File     :barChartStackTest.py
# Location:/Home/PycharmProjects/..

# LeeCode No.84


class Solution:
    # Use stack to solve problems
    # Construct a list in ASCENDING
    # According:https://blog.csdn.net/jingsuwen1/article/details/51577983
    # Modified Java to Python
    @staticmethod
    def stack_solve(heights):
        if len(heights) == 0:
            return 0
        elif len(heights) == 1:
            return heights[0]
        else:
            # List construct to stack
            # Result to save area
            stack = []
            result = 0
            for height in heights:
                if stack == []:
                    stack.append(height)
                else:
                    # If the last element
                    # Smaller than or equal with
                    # Waiting push one
                    # Directly push
                    if stack[len(stack)-1] <= height:
                        stack.append(height)
                    # If the last element
                    # Bigger than  waiting push one
                    # Iterate forwards and replace
                    else:
                        # Using to save length
                        # Temp area = index * height
                        index = 0
                        # Iterate forwards
                        # Util the next one is much smaller
                        i = 1
                        while stack[len(stack) - i] > height:
                            # If stack[i] >= height
                            # Stack pop the bigger
                            # And push the replacement
                            # Index += 1
                            # Temp area = max(result, index * height)
                            index += 1
                            result = max(result, stack[len(stack) - i]*index)
                            stack[len(stack) - i] = height
                            i += 1
                        # Initial index = 1
                        index = 0
                        # Initial i = 1
                        i = 1
                        stack.append(height)
            for i in range(0, len(stack)):
                result = max(result, stack[i]*(len(stack)-i))
            return result


if __name__ == '__main__':
    print(Solution.stack_solve([0, 9]))

