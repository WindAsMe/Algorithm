# !/usr/bin/python3
# -- coding: UTF-8 --
# Author   :WindAsMe
# Date     :18-6-13 下午2:11
# File     :firstUniqChar.py
# Location:/Home/PycharmProjects/..

# LeeCode No.387


class Solution:
    @staticmethod
    def firstUniqChar(s):
        """
        :type s: str
        :rtype: int
        """
        for i in range(len(s)):
            # 1. this word not occur the before and after (AC)
            if s[i] not in s[i + 1:] and s[i] not in s[:i]:
                return i

            # 2. Calculate the occurs time (TL)
            # if s.count(s[i], 0, len(s)) == 1:
            #     return i
        return -1


if __name__ == '__main__':
    print(Solution.firstUniqChar("qwe"))