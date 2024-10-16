class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # i literally don't know how to this off the top of my head
        # so i think you want to utilize some of python's ability to swap places between two things
        # let's see how the indicies move
        # 0, 0 -> 0, 2     0, 1 -> 1, 2     0, 2 -> 2, 0
        # so you have center indices, or you can have corner indices, or you can have odd corner index which doesn't move
        """
        so to swap the corners of a 3x3, you swap 1,3 then swap 9,7 then swap 7 and 3
        you can do this with everything actually, you need 3 swaps to get the right configuration for 4 points

        let's try with a 2x2, then a 3x3, then 4x4, and see if we can generalize it
        """
        matrix[0][0], matrix[0][1] = matrix[0][1], matrix[0][0]
        print(matrix)
        matrix[0][0], matrix[1][0] = matrix[1][0], matrix[0][0]
        print(matrix)
        matrix[1][0], matrix[1][1] = matrix[1][1], matrix[1][0]
        print(matrix)

