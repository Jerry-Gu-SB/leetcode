class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # looks like you can just iterate from the start and every time you hit a negative just have
        # a flag for whether you've hit even or odd negatives. when you hit odd, store the current product in temp. reset current prod to 0.
        # when you hit an even, multiply last_prod * cur_prod.
        # every time you do a multiply, check it against solution.

        # 3 var: solution, cur_prod, last_prod
        # did not account for 0. i guess if it's zero then you just compare with the solution and if it's bigger at that the zero then you just make it the solution.
        solution = float('-inf')
        temp = 0
        even = True

        for i in range(len(nums)):
            if i == 0:
                cur_prod = nums[i]
                continue

            if nums[i] == 0:
                even = True
            elif nums[i] > 0:
                cur_prod *= nums[i]
            elif nums[i] < 0:
                if even:
                    temp = cur_prod
                    curprod = nums[i]
                    even = False
                else:
                    even = True
                    curprod *= temp
                    temp = 0
            solution = max(solution, cur_prod)
        return solution

