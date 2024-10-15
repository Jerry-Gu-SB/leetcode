class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # validate 3 separate times, then try to validate in one pass

        # # validate boxes
        # for row in range(0, 9, 3):
        #     for column in range(0, 9, 3):
        #         seen = set()
        #         for i in range(row, row + 3):
        #             for j in range(column, column + 3):
        #                 if board[i][j] in seen:
        #                     print("seen:", seen)
        #                     print("box false:", "i:", i, "j:", j, "row:", row, "column", column)
        #                     return False
        #                 elif board[i][j] != ".":
        #                     seen.add(board[i][j])

        # # validate rows
        # for i in range(9):
        #     seen = set()
        #     for j in range(9):
        #         if board[i][j] in seen:
        #             print("row false:", "i:", i, "j:", j)
        #             return False
        #         elif board[i][j] != ".":
        #             seen.add(board[i][j])

        # # validate columns
        # for i in range(9):
        #     seen = set()
        #     for j in range(9):
        #         if board[j][i] in seen:
        #             print("column false:", "i:", i, "j:", j)
        #             return False
        #         elif board[j][i] != ".":
        #             seen.add(board[j][i])
        # return True

        # one pass

        # validate boxes
        column_dict = {1: set(), 2: set(), 3: set(), 4: set(), 5: set(), 6: set(), 7: set(), 8: set(), 0: set()}
        row_dict = {1: set(), 2: set(), 3: set(), 4: set(), 5: set(), 6: set(), 7: set(), 8: set(), 0: set()}

        for row in range(0, 9, 3):
            for column in range(0, 9, 3):
                seen = set()
                for i in range(row, row + 3):
                    for j in range(column, column + 3):
                        cur = board[i][j]
                        if cur in seen or cur in row_dict[i] or cur in column_dict[j]:
                            return False
                        elif board[i][j] != ".":
                            seen.add(cur)
                            row_dict[i].add(cur)
                            column_dict[j].add(cur)

        return True