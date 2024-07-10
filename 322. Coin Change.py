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

    # my recursive attempt
    from collections import defaultdict
    class Solution:
        def coinChange(self, coins: List[int], amount: int) -> int:
            def defaultVal():
                return float('inf')

            if amount == 0: return 0
            memo = defaultdict(defaultVal)
            for coin in coins:
                memo[coin] = 1

            def rec(target):
                if target in memo.keys():
                    return memo[target]
                if target == 0:
                    return 0
                if target < 0:
                    return float('inf')

                min_coins = float('inf')
                for coin in coins:
                    temp = rec(target - coin)
                    if temp != float('inf'):
                        min_coins = min(min_coins, temp + 1)
                memo[target] = min_coins
                return memo[target]

            sol = rec(amount)

            if sol == float('inf'):
                return -1
            return sol


