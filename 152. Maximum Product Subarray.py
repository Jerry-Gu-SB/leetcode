class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # looks like you can just iterate from the start and every time you hit a negative just have
        # a flag for whether you've hit even or odd negatives. when you hit odd, store the current product in temp. reset current prod to 0.
        # when you hit an even, multiply last_prod * cur_prod.
        # every time you do a multiply, check it against solution.

        # 3 var: solution, cur_prod, last_prod
        # did not account for 0. i guess if it's zero then you just compare with the solution and if it's bigger at that the zero then you just make it the solution.
        # if len(nums) == 1:
        #     return nums[0]
        # solution = max(nums)
        # temp = 0
        # even = True
        # cur_prod = nums[0]

        # for i in range(len(nums)):
        #     print(i, ". ", "cur_prod: " + str(cur_prod), "temp: " + str(temp), "solution: " + str(solution), "even: " + str(even))
        #     if i == 0:
        #         if nums[i] < 0:
        #             even = False
        #         continue
        #     cur_prod *= nums[i]
        #     if nums[i] == 0:
        #         even = True
        #     elif nums[i] < 0:
        #         if not even:
        #             temp = cur_prod
        #             cur_prod = nums[i]
        #             even = True
        #         else:
        #             cur_prod *= temp
        #             temp = 0
        #             even = False

        #     solution = max(solution, cur_prod)
        #     print(i, ". ", "cur_prod: " + str(cur_prod), "temp: " + str(temp), "solution: " + str(solution), "even: " + str(even))
        # print("last--", "cur_prod: " + str(cur_prod), "temp: " + str(temp), "solution: " + str(solution), "even: " + str(even))
        # return solution

        # brute force: check every subarray
        # def prod(listo):
        #     prod = 1
        #     for num in listo:
        #         prod *= num
        #     return prod

        # maxo = float('-inf')
        # for i in range(len(nums)):
        #     for j in range(i, len(nums) + 1):
        #         if i < j:
        #             maxo = max(maxo, prod(nums[i : j]))
        # return maxo

        # okay i watched the neetcode vid.
        # basically you want to store the min/max of each subarray so that way when you iterate across, you can multiply by the min/max an djust choose as your means of accounting for the negatives
        # for the zeroes, you'd just reset the min/max.

        mino = 1
        maxo = 1
        solution = max(nums)
        for i in range(len(nums)):
            if nums[i] == 0:
                maxo = 1
                mino = 1
            temp = maxo
            maxo = max(nums[i], mino * nums[i], maxo * nums[i])
            mino = min(nums[i], mino * nums[i], temp * nums[i])
            solution = max(maxo, solution)

        return solution
