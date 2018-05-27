# !/usr/bin/python3
# -- coding: UTF-8 --
# Author   :WindAsMe
# Date     :18-5-14 下午2:51
# File     :createTest.py
# Location:/Home/PycharmProjects/..

# LeeCode No.118


class Solution:
    @staticmethod
    def generate(numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        list = []
        before = [1, 1]
        if numRows == 0:
            return list
        # NumRows == 1
        # Return [
        #          [1]
        #              ]
        elif numRows == 1:
            list.append([1])
            return list
        # NumRows == 2
        # Return [
        #          [1],
        #         [1, 1]
        #               ]
        elif numRows == 2:
            list.append([1])
            list.append([1, 1])
            return list
        # NumRows >= 3
        else:
            # Save the NEWEST ROW
            list.append([1])
            list.append([1, 1])
            new = []
            # Row target
            for rowIndex in range(3, numRows+1):
                print('rowIndex:', rowIndex)
                # Certain row which index
                for row in range(rowIndex):
                    print('row:', row)
                    if row == 0:
                        new.append(1)
                    elif row == rowIndex-1:
                        new.append(1)
                    else:
                        new.append(before[row-1]+before[row])
                # DEEP COPY
                # Just '=' is NOT CONFORM
                before = new.copy()
                new.clear()
                list.append(before)
                print('before:', before)
            return list


if __name__ == '__main__':

    print(Solution.generate(5))

