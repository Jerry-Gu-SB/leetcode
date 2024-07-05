class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        # try to do this using a recursive method next time too

        dp = [float('inf') for i in range(amount + 1)]
        dp[0] = 0
        for i in range(1, amount + 1):
            for coin in coins:
                if i - coin >= 0:
                    dp[i] = min(dp[i], 1 + dp[i - coin])
        return dp[amount] if dp[amount] < float('inf') else -1