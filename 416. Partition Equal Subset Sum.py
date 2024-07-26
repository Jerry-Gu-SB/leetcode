class Solution:
    from itertools import combinations
    def canPartition(self, nums: List[int]) -> bool:
        # brute force:
        # check every single subset, sum it against its opposite
        # NOT SUBSET, PERMUTATION
        # DID THE TREE, STARTING TO UNDERSTAND SOMETHING. LET ME COOK TOMORROW.
        # half = sum(nums) / 2
        # memo = set()
        # for i in range(len(nums)):
        #     combo = combinations(nums, i)
        #     for comb in combo:
        #         if sum(comb) == half:
        #             return True
        # return False

        # we simply need to track the combinations but for the indices i think should be memoized
        # you also don't need to keep going once you're past the sum.
        # yeah i thinmk it's some form of like memo[0] + cur index, but you need to do it on a 2d scale maybe? man this shit is hard

        # figure out the sub problems a bit more i guess.
        # if there is a solution, you can actually start with any number and you will have an answer
        # and if you don't find an answer, there is no answer actually.

        # OKAY WE KIDNA COOKIN BUT WE NEED TO MEMOIZE SOMEWHERE

        # WOW OKAY I WAS READY TO GIVE UP ON THIS PROBLEM BUT WE MADE A LOT OF PROGRESS

        # yea okay i get a wall again. I think you can give max 1 more session, else just get the solution

        # def rec(target, index):
        #     if target < 0:
        #         return False
        #     elif target == 0:
        #         return True
        #     sol = False
        #     for i in range(len(nums)):
        #         if i not in index:
        #             print(i, target, index)
        #             index.append(i)
        #             sol = rec(target - nums[i], index) or sol
        #     return sol
        # if rec(sum(nums))
        # for i in range(len(nums)):
        #     if rec(sum(nums) / 2, [i]):
        #         return True
        # return False

        # okay your decision tree was all wrong. you iterate from the beginning and choose or not choose
        # that number. the rest was okay with the subtraction it seemed. go from there now.
        # global incremento
        # memo = [[]]
        # incremento = 0
        # targeto = sum(nums) / 2
        # def rec(target, numo):
        #     global incremento
        #     incremento += 1
        #     # print(target, numo)
        #     if target == 0:
        #         return True
        #     if numo in memo:
        #         return False
        #     if target < 0:
        #         return False

        #     sol = False
        #     for i in range(len(numo)):
        #         spliced = numo[:i] + numo[i + 1 :]
        #         if spliced in memo:
        #             continue
        #         sol = sol or rec(target - numo[i], spliced) or rec(target, spliced)
        #         memo.append(numo)
        #         # print(sol)
        #     return sol
        # ret = rec(targeto, nums)
        # # print("incremento: " + str(incremento))
        # return ret

        # just finished the neetcode video, i would have never have arrived there.
        # adding every single number, and then adding all the numbers to that to get
        # all sums is actually genius, i would have never gotten that. that's so fucking smart man
        # i'm a little mad and annoyed. I was just not thinking on that deep level.
        if sum(nums) % 2 != 0: return False

        target = sum(nums) / 2

        dp = set()
        dp.add(0)
        for num in nums:
            # print(target, nums)
            temp = set()
            if target in dp: return True
            for numo in dp:
                temp.add(numo + num)
                temp.add(numo)
            dp = temp

        if target not in dp:
            return False
        else:
            return True



