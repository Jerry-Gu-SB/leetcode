class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # so the sub problems arise as soon as you make a move, you cut off the row or column behind you
        # so it looks like you dp for an algo of O(m * n) times i think
        #  think you actually start at the beginning and you DP by accessing the previous stuff
        # so it's where you are, plus right + down if it exists. you need to memoize the previous PATH
        # it seems?
        # think it's basically you just dp for each choice of going down and right for each
        # box. and then you DP to look at the last box that is up or left from you.

        # 2 approaches:
        #   start from the top and recurse rec(2, 3) and return rec(1, 3) + rec(2, 2)
        #   start from the bottom and keep adding 1 from the previous box.

        # okay i think i actually have a good gameplan here. let's try and do this tomorrow or maybe the day after because i have to move tomorrow and idk what the heck's gonna happen.

