class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1: return 1
        if n == 2: return 2
        memo = [float('-inf') for i in range(n)]
        memo[0] = 1
        memo[1] = 2

        for i in range(n):
            if memo[i] < 0:
                memo[i] = memo[i - 1] + memo[i - 2]
        return memo[n - 1]

# first time solving this:
# class Solution:
#     def climbStairs(self, n: int) -> int:
#         # 1 = 1: 1
#         # 2 = 2: 11, 2
#         # 3 = 3: 12, 21, 111
#         # 4 = 5: 1111, 112, 121, 211, 22
#         # 5 = 8: 11111, 2111, 1211, 1121, 1112, 221, 212, 122
#         # 6 = 13?: 111111, 21111, 12111, 11211, 11121, 11112, 1122, 1212, 2112, 2121, 2211, 1221, 222
#         sums = [0 for i in range(n)]
#         for i in range(n):
#             if i == 0:
#                 sums[i] = 1
#             elif i == 1:
#                 sums[i] = 2
#             else:
#                 sums[i] = sums[i - 1] + sums[i - 2]
#         return sums[n - 1]
