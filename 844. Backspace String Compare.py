class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        # iterate through teh string with a WHILE loop
        # if you hit a letter, move on
        # if you hit a backspace, if at 0th index, do nothing
        # otherwise, delete the previous character, delete the backspace character, index--
        # start from index again.

        # to delete tcurrent and previous: index--, pop(index) twice
        # return s == t

        i = 0
        j = 0
        while i <= len(s) or j <= len(t):
            if 0 < i < len(s) and s[i] == '#':
                i -= 1
                s = s[:i] + s[i + 1:]
                s = s[:i] + s[i + 1:]
            elif i == 0 and len(s) > 0 and s[i] == '#':
                s = s[1:]
            else:
                i += 1
            if 0 < j < len(t) and t[j] == '#':
                j -= 1
                t = t[:j] + t[j + 1:]
                t = t[:j] + t[j + 1:]
            elif j == 0 and len(t) > 0 and t[j] == '#':
                t = t[1:]
            else:
                j += 1
        return s == t