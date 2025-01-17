class Solution:
    from collections import defaultdict
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        # yeah well it looks like it's lookin a little exponential runtime here

        # wait this is like bigger boxes like in DSA 2 that i took. don't you just use DP here?
        # probably start with the smallest box, then start branching out.
        # if there are multiple smallest boxes, then grab all of them.
        # careful about really tall thin boxes, or ultra wide flat boxes.

        # okay so this is just kinda completely the wrong approach, but it's okay, seeing the trick is notoriously hard for this problem

        # for i in range(len(envelopes)):
        #     envelopes[i] = tuple(envelopes[i])

        # def fits(letter_1, letter_2):
        #     if letter_1[0] < letter_2[0] and letter_1[1] < letter_2[1]:
        #         return True
        #     else:
        #         return False

        # memo = defaultdict(lambda: 1)
        # sol = 1

        # def rec(cur_envelope, envelopes_left):
        #     if cur_envelope in memo.keys():
        #         return memo[cur_envelope]

        #     ret = 1
        #     for i, envelope in enumerate(envelopes_left):
        #         if fits(cur_envelope, envelope):
        #             ret = max(ret, 1 + rec(envelope, envelopes_left[:i] + envelopes_left[i + 1:]))
        #             memo[cur_envelope] = ret
        #     return ret

        # for i, env in enumerate(envelopes):
        #     cur_val = rec(env, envelopes[:i] + envelopes[i + 1:])
        #     memo[env] = cur_val
        #     sol = max(sol, cur_val)
        # return sol

        # THE TRICK
        # you just resort the envelopes by ascending WIDTH and descending HEIGHT
        # the nyou find longest increasing subsequence https://leetcode.com/problems/longest-increasing-subsequence/description/
        # https://www.youtube.com/watch?v=3fF1r5nhQX4 for explanation
        # https://www.youtube.com/watch?v=c7fONABS5Z8 for the code

        env = sorted(envelopes, key=lambda x: (x[0], -x[1]))

        dp = []

        for w, h in env:
            i = bisect_left(dp, h)  # binary search for h in the dp, then insert left of that

            if i == len(dp):
                dp.append(h)
            else:
                dp[i] = h

        return len(dp)
