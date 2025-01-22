class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # the string lengths are pretty short so i think you can just do a O(200 * 200) = O(1)
        stringo = strs[0]
        sol = ""
        for i in range(len(stringo)):
            for s in strs:
                if len(s) == i or s[i] != stringo[i]:
                    return sol
            sol += stringo[i]
        return sol