class Solution:
    # test cases
    # [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16], [17, 18, 19, 20], [21, 22, 23, 24]]
    # [[1, 2, 3, 4]]
    # [[1], [2], [3], [4]]
    # [[1, 2, 3, 4], [5, 6, 7, 8]]
    # [[1, 2], [3, 4]]
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # bottom, top, left, right
        # use those varaibles to track which direction you need to go to.
        # or maybe you just do

        sol = []
        total = len(matrix) * len(matrix[0])
        STATE = "TOP"

        top = 0
        bottom = len(matrix)
        left = 0
        right = len(matrix[0])

        while len(sol) < total:
            if STATE == "TOP":
                for i in range(left, right):
                    sol.append(matrix[top][i])
                if top < bottom:
                    top += 1
                STATE = "RIGHT"

            elif STATE == "RIGHT":
                for i in range(top, bottom):
                    sol.append(matrix[i][right - 1])
                if right > left:
                    right -= 1
                STATE = "BOT"

            elif STATE == "BOT":
                for i in reversed(range(left, right)):
                    sol.append(matrix[bottom - 1][i])
                if bottom > top:
                    bottom -= 1
                STATE = "LEFT"

            elif STATE == "LEFT":
                print("bottom:", bottom, "top:", top, "left:", left, "right:", right)
                for i in reversed(range(bottom, top)):
                    sol.append(matrix[i][left])
                if right < left:
                    left += 1
                STATE = "TOP"

            print(sol)
        return sol