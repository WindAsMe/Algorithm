# !/usr/bin/python3
# -- coding: UTF-8 --
# Author   :WindAsMe
# Date     :18-5-16 下午8:30
# File     :findDiagonalOrderTest.py
# Location:/Home/PycharmProjects/..

# LeeCode No.498


class Solution:
    @staticmethod
    def find_diagonal_order(matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        # Form like this:
        # [
        #    [ 1, 2, 3 ],
        #    [ 4, 5, 6 ],
        #    [ 7, 8, 9 ]
        #                  ]

        # x save the row of matrix
        # y save the column of matrix

        # For special data use case
        if len(matrix) == 0:
            return []
        elif len(matrix) == 1:
            return matrix[0]
        # If matrix like[
        #                   [1],
        #                   [2],
        #                   [3]
        #                          ]
        elif len(matrix[0]) == 1:
            a = []
            for x in range(len(matrix)):
                a.append(matrix[x][0])
            return a

        x = len(matrix)
        y = len(matrix[0])

        # Row and column save the current index
        row = 0
        column = 1

        # If flag = 0:
        # Read from left foot to right head
        # If flag = 1:
        # Read from right head to left foot
        flag = 1

        result = [matrix[0][0]]
        while (row + 1) * (column + 1) < x * y:
            # Read data from right head to left foot
            result.append(matrix[row][column])
            if flag == 1:
                if row + 1 >= x or column - 1 < 0:
                    # Change the forwards
                    flag = 0
                    row += 1

                    # If the matrix is like
                    # [
                    #   [1, 2, 3, 4, 5],
                    #   [5, 4 ,3 ,2, 1],
                    #   [9, 8, 9, 9, 9]
                    #                   ]
                    # When iteration in '8'
                    # DON'T do row += 1
                    # INSTEAD do column += 1

                    # Descend the add before
                    if row == x:
                        row -= 1
                        column += 1
                else:
                    row += 1
                    column -= 1
            # Read data from left foot to right head
            else:
                if row - 1 < 0 or column + 1 >= y:
                    flag = 1
                    column += 1
                    # Operation like before
                    if column == y:
                        column -= 1
                        row += 1
                else:
                    row -= 1
                    column += 1

        result.append(matrix[row][column])
        return result


if __name__ == '__main__':
    print(Solution.find_diagonal_order([[2], [3]]))

