class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
# i actually figured out that i'd need a sliding window, but i didn't
# know how to know whether it was teh right approach. in this sense,
# I could've done a bit better. you've seen the solution,
# so recreate tomorrow.


#         # oops i didn't read the question well enough
#         # it's not without repeating characters, it's UNIQUE characters
#         # initialize dictionary with whole alphabet. or just have a set of characters you have

#         # this is a weird one, you have to account for overlapping like "dvdf"
#         # you could maybe have a set for each character??? would be too much memory. would also be n^2
#         bcawabcde
#         # Hint 1
#         # Generate all possible substrings & check for each substring if it's valid and
#         # keep updating maxLen accordingly. brute force o(n^2) far too slow
# if len(s) == 1:
#     return 1
# maxLen = 0
# for start in range(len(s)):
#     for end in range(start, len(s)):
#         substring = s[start : end + 1]
#         if sorted(list(set(substring))) == sorted(list(substring)):
#             maxLen = max(maxLen, end - start + 1)
# return maxLen


#         # still doesn't work and is n^2 anyway
#         temp = 0
#         sol = 0
#         alp = set()
#         for i in range(len(s)):
#             string = s[i::]
#             for char in string:
#                 if char in alp:
#                     temp = 1
#                     alp = set()
#                     alp.add(char)
#                 else:
#                     alp.add(char)
#                     temp += 1
#                     if sol < temp:
#                         sol = temp
#         return sol