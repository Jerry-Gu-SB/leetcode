class Solution:
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

        while len(sol) <= total:
            if STATE == "TOP":
                for i in range(left, right):
                    sol.append(matrix[top][i])
                top += 1
                STATE = "RIGHT"

            elif STATE == "RIGHT":
                for i in range(top, bottom):
                    sol.append(matrix[i][right - 1])
                right -= 1
                STATE = "BOT"

            elif STATE == "BOT":
                for i in range(left, right, -1):
                    sol.append(matrix[bottom - 1][i])
                bottom -= 1
                STATE = "LEFT"

            elif STATE == "LEFT":
                for i in range(bottom, top):
                    sol.append(matrix[i][left])
                left += 1
                STATE = "TOP"

            print(sol)
        return sol