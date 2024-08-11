class Solution:
    def canJump(self, nums: List[int]) -> bool:
        dp = set()
        memo = []
        memo.append(0)
        iteration = 0
        while len(memo) > 0:
            cur = memo.pop(0)
            cur_val = nums[cur]
            if cur == len(nums) - 1:
                return True
            for i in range(cur_val + 1):
                jump = i + cur
                if jump not in dp:
                    memo.append(jump)
                    dp.add(jump)
        return False

        # wait the only way to not make it is if you hit zero?? you can wait unti you calculate the chasm length and then backtrack to find a number that makes it.
        # OR you can just keep track of the biggest jump possible so far. once you hit a zero, you calculate the chasm after the zero, and then see if the biggest jump possible you have can get over that chasm.
        # not biggest jump as in distance wise, but teh farthest you could possibly jump. see example 2 for reference.
