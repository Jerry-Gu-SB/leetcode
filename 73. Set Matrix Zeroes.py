class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # well i mean the naive way is to just do it. i think you could speed it up by skipping already changed
        # rows/columns. let's just do it the straight naive way first

        # for row in range(len(matrix)):
        #     for col in range(len(matrix[0])):
        #         if matrix[row][col] == 0:
        #             for i in range(len(matrix[0])):
        #                 matrix[row][i] = 0
        #             for j in range(len(matrix)):
        #                 matrix[j][col] = 0

        # OH I SEE. SO YOU CAN'T JUST DO THIS BECAUS EIT'LL START SETTING EVERYTHING TO ZERO
        change = set()
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if matrix[row][col] == 0:
                    for i in range(len(matrix[0])):
                        change.add((row, i))
                    for j in range(len(matrix)):
                        change.add((j, col))

        for point in change:
            matrix[point[0]][point[1]] = 0

        # okay this is weirdly fast for a cubic solution. well i don't actually think you can get faster than a cubic
        # runtime to be honest

        # OKAY JUST KIDDING WHAT, it seems like the runtime isn't the bottleneck, but it was the space.
        # you jus tdidn't read the followup. i think for these problems, if the initial solution is easy,
        # there's probably a followup. I watched the neetcode solution and holy moly that's smart asf
        # let's try that next time