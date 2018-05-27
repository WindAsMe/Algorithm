# !/usr/bin/python3
# -- coding: UTF-8 --
# Author   :WindAsMe
# Date     :18-5-27 下午3:39
# File     :longestCommonPrefix.py
# Location:/Home/PycharmProjects/..

# LeeCode No.14


class Solution:

    @staticmethod
    def longestCommonPrefix(strs):
        """
        strs is like:
        [
            "asd",
            "fgh",
            "zxc"
        ]
        :type strs: List[str]
        :rtype: str
        """

        font = ""

        if strs == [] or strs == [""]:
            return font

        if len(strs) == 1:
            return strs[0]
        min_length = len(strs[0])
        # Find the least length of matrix
        for i in range(len(strs)):
            min_length = min(min_length, len(strs[i]))

        if min_length == 0:
            return font


        flag = 0
        # Iterate the in two dimension
        for i in range(min_length):

            # If has the same font
            # strs[0] must has the same
            temp = strs[0][i]
            for j in  range(len(strs)):
                if strs[j][i] == temp:
                    pass
                else:
                    flag = 1
                    break
            if flag == 1:
                return font
            else:
                font += temp
        return font


if __name__ == '__main__':
    strs = [
        "acc","ac"
    ]
    print(Solution.longestCommonPrefix(strs))
