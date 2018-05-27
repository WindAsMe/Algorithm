# !/usr/bin/python3
# -- coding: UTF-8 --
# Author   :WindAsMe
# Date     :18-5-15 下午1:29
# File     :surroundDFSTest.py
# Location:/Home/PycharmProjects/..

# LeeCode No.130


class Solution:
    @staticmethod
    def solve(board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        # List like [
        #               []
        #               []
        #               []
        #               []    ]

        if board == []:
            return []
        # x save row number
        # y save column
        x = len(board[0])
        y = len(board)
        # print('x:', x, 'y', y)

        # Saving index:(row, column) waiting judge point
        wait_paint = []
        # Find 'O' for each
        for row in range(y):
            for column in range(x):
                print(print('in circulation', row, 'and',  column))
                if board[row][column] == 'O':
                    print('in judge', row, 'and',  column)
                    # Judge is change the element or not
                    # Get the list:wait_paint
                    # If return value is True, paint to 'X'
                    # Else, paint to 'O'
                    if Solution.is_paint(board, row, column, wait_paint) is True:
                        # print('need paint', wait_paint)
                        # a is like (1, 3)
                        # If need paint
                        # Have painted in FUNCTION
                        # Clear for next circulation
                        wait_paint.clear()
                    else:
                        # print('needn\'t paint', wait_paint)
                        # If needn't paint
                        # After function, restore
                        # a is like (1, 3)
                        for a in wait_paint:
                            board[a[0]][a[1]] = 'O'
                        wait_paint.clear()
                else:
                    pass
        return board

    @staticmethod
    def is_paint(board, row, column, wait_paint):

        # This block is on the edge
        if row == 0 or row == len(board) - 1 or column == 0 or column == len(board[0]) - 1:
            # UNNECESSARY painting
            return
        # This block is isolated
        # NEED painting
        elif board[row - 1][column] == 'X' and board[row + 1][column] == 'X' and board[row][column - 1] == 'X' and \
                board[row][column + 1] == 'X':
            # print('point:', '(', row, ',', column, ')')
            # This block need painted
            # Return True
            board[row][column] = 'X'
            wait_paint.append((row, column))
            return True
        # This block has 'O' around

        # The Iterate from left to right
        # From head to foot
        # So LEFT and HEAD's Judgement is UNNECESSARY

        # 'O' is in foot
        elif board[row + 1][column] == 'O':
            board[row][column] = 'X'
            wait_paint.append((row, column))
            # Judge the board[row + 1][column]
            # This block is isolated
            # index:(row, column) append to wait_paint
            if Solution.is_paint(board, row + 1, column, wait_paint) is True:
                return True
            # This block is paint UNNECESSARILY
            else:
                return
        # 'O' is on right
        elif board[row][column + 1] == 'O':
            board[row][column] = 'X'
            wait_paint.append((row, column))
            if Solution.is_paint(board, row, column + 1, wait_paint) is True:
                return True
            else:
                return
        # If proceeding here
        # Mean this block's surrounding
        # Must by the line
        # UNNECESSARY painting
        else:
            return


if __name__ == '__main__':

    print('board',
          Solution.solve([["X", "X", "X", "X"], ["X", "O", "O", "X"], ["X", "X", "O", "X"], ["X", "O", "X", "X"]]))
