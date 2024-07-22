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

        # okay your decision tree was all wrong. you iterate from the beginning and choose or not choose
        # that number. the rest was okay with the subtraction it seemed. go from there now.
        def rec(target, index):
            if target < 0:
                return False
            elif target == 0:
                return True
            sol = False
            for i in range(len(nums)):
                if i not in index:
                    print(i, target, index)
                    index.append(i)
                    sol = rec(target - nums[i], index) or sol
            return sol

        if rec(sum(nums)):
            for i in range(len(nums)):
                if rec(sum(nums) / 2, [i]):
                    return True
        return False




