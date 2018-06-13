# !/usr/bin/python3
# -- coding: UTF-8 --
# Author   :WindAsMe
# Date     :18-6-13 下午3:43
# File     :canConstruct.py
# Location:/Home/PycharmProjects/..

# LeeCode No.383

# Need continuous words
class Solution:
    @staticmethod
    def canConstruct(ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        return ransomNote in magazine



if __name__ == '__main__':
    print(Solution.canConstruct("aa", "aab"))
