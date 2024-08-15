class Solution:
    def countBits(self, n: int) -> List[int]:

        # 0 --> 0
        # 1 --> 1
        # 2 --> 10
        # 3 --> 11
        # 4 --> 100
        # 5 --> 101
        # 6 --> 110
        # 7 --> 111
        # 8 --> 1000
        # 9 --> 1001
        # 10 --> 1010
        # 11 --> 1011
        # [0, 1, 1, 2, 1, 2, 2, 2, 3, 1, 2, 2, 3 ]
        if n == 0: return [0]
        if n == 1: return [0, 1]
        sol = [0 for i in range(n + 1)]
        sol[0] = 0
        sol[1] = 1
        for num in range(2, n + 1):
            if num % 2 == 0:
                sol[num] = sol[num // 2]
            else:
                sol[num] = sol[num // 2] + 1
        return sol
