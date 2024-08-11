class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # brute force: check every single subsequence
        sol = 1
        dp = [1]
        for i in range(1, len(nums)):
            temp = 0
            for j in range(len(dp)):
                if nums[j] < nums[i]:
                    temp = max(temp, dp[j])
            dp.append(temp + 1)
        sol = max(dp)
        return sol