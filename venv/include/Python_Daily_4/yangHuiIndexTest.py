# !/usr/bin/python3
# -- coding: UTF-8 --
# Author   :WindAsMe
# Date     :18-5-14 下午3:46
# File     :yangHuiIndexTest.py
# Location:/Home/PycharmProjects/..

# LeeCode No.119


class Solution:
    @staticmethod
    def get_row(rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        before = [1, 1]
        list = []
        # GET certain row's element
        # NOT all
        if rowIndex == 0:
            return list
        elif rowIndex == 1:
            list.append(1)
            return list
        elif rowIndex == 2:
            list.append(1)
            list.append(1)
            return list
        # rowIndex >= 3
        else:

            for rowNum in range(3, rowIndex+2):
                print('rowNum', rowNum)
                for row in range(rowNum):
                    print('row', row)
                    if row == 0:
                        list.append(1)
                    elif row == rowNum-1:
                        list.append(1)
                    else:
                        list.append(before[row-1]+before[row])
                before = list.copy()
                list.clear()
            return before


if __name__ == '__main__':
    print(Solution.get_row(2))
