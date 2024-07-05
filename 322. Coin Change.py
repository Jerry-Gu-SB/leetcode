from collections import defaultdict


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0: return 0
        if len(coins) == 1:
            if coins[0] == amount:
                return -1
            else:
                return 0

        memo = defaultdict(int)

        def rec(cur_amount, coin_list):
            global memo
            if cur_amount in memo.keys():
                return memo[cur_amount]
            if cur_amount == coin[0]:
                memo[cur_amount] = 1
                return 1

            cur_amount -= coin_list[-1]

            if coin_list[-1] > cur_amount:
                coin_list = coin_list[0:len(coin_list) - 1]

            temp = rec(cur_amount, coin_list)
            memo[cur_amount] = temp
            return temp

        return rec(coins, amount)



