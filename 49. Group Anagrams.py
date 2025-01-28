class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # create copy of list
        # iterate through the list
        #   sort every string in list
        # grab the index of every sorted string, and append it to a dictionary of that string
        # return the dictionary entry for that string

        new_strs = []

        for word in strs:
            new_strs.append(word)

        for i in range(len(new_strs)):
            temp = new_strs[i]
            new_strs[i] = ""
            for char in sorted(temp):
                new_strs[i] += char

        dicto = {}
        for i, word in enumerate(new_strs):
            if word in dicto:
                dicto[word].append(i)
            else:
                dicto[word] = [i]
        solution = []
        for key, value in dicto.items():
            cur = []
            for index in value:
                cur.append(strs[index])
            solution.append(cur)
        return solution