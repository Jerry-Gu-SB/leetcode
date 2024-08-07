# ah shit here we go again

# MAN YOU ARE WAY OVERCOMPLICATING THIS. HOW IS THIS SO HARD??? look at the solutions tomorrow and relaly study them.
# then rework the problem
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # bottom up approach DP
        storage_memo = [[float('-inf') for num in nums] for num in nums]
        for i in range(len(nums)):
            storage_memo[i][i] = nums[i]

        def dp(first, second):
            print(first, second)
            if storage_memo[first][second] == float('-inf'):
                return storage_memo[first][second]
            cur_max = float('-inf')
            for i in range(len(nums)):
                for j in range(len(nums)):
                    cur_max = max(dp(i, j), cur_max, sum(nums[first: second]))
            storage_memo[first][second] = cur_max
            return cur_max

        sol = dp(0, len(nums) - 1)
        print(sol, storage_memo)
        return sol


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:



        # brute force: look through every single subarray
        # check current largest sum
        # if it's bigger, then that's the new sum
        # return largest sum
        # sol = sum(nums)
        # print(sol)
        # for i in range(len(nums) + 1):
        #     for j in range(len(nums) + 1):
        #         if i < j:
        #             cur_sum = sum(nums[i : j])
        #             if cur_sum > sol:
        #                 sol = cur_sum
        # return sol

        # kadane's algorithm. this was kind of what i was getting at before,
        # convince yourself this works

        # also do it using the sliding window method, the dynamic progrmaming method,
        # and the divide and conquer method. we're gonna be doing this problem
        # for a hot minute

        # dynamic programming:
        # find the work you have to do
        # find a way to store the work youve already done

        # checking every subarray is just the smaller subarray plus an extra character
        # so if you check 12345, when you check 1, 12, 123, 1234, 12345, you can recursively
        # check 23, 234, 2345 as well and then memoize for next iteration
        #      j:  0  1  2  3   4  5  6  7  8
        # i:0     -2 -1 -4  0  -1  1  2 -3  1
        #   1         1 -2  2   1  3  4 -1  3
        #   2           -3  1   0  2  3 -2  2

        # try flipping the triangle over to get a better visual

        # getting closer but need to write it down, can't do thsi in class..
        cur_sum = 0
        solution = -inf
        grid = [[] for i in range(len(nums))]
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                # print(grid)
                print("solution: ", solution)
                print("cur_sum: ", cur_sum)
                if i == 0:
                    cur_sum += nums[j]
                else:
                    print("i: ", i, " j: ", j)
                    cur_sum = nums[j - i] - grid[i - 1][j - 1]
                grid[i].append(cur_sum)
                solution = max(solution, cur_sum)
        print(grid)
        print("solution: ", solution)
        return solution

        # also you were trying to intuit the sliding window. you need to do more
        # sliding window problems because you aren't recognizing that pattern.
        # if not nums: return []

        # cur = 0
        # solution = -inf
        # for num in nums:
        #     cur = max(num, cur + num)
        #     solution = max(solution, cur)

        # return solution
