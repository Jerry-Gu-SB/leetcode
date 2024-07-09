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
            global memo
            memo = defaultdict(defaultVal)
            for coin in coins:
                memo[coin] = 1

            def rec(coin_list, target):
                if target in memo.keys():
                    return memo[target]
                if target < 0:
                    return float('-inf')
                for coin in coin_list:
                    temp = rec(coin_list, target - coin) + 1
                    memo[target] = min(memo[target], temp)
                return memo[target]

            sol = rec(coins, amount)
            print(memo)

            if sol <= 0:
                return -1
            return sol


