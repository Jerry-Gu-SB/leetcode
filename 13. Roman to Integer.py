class Solution:
    def romanToInt(self, s: str) -> int:
        numerals = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        sol = 0
        # naive case
        for i, char in enumerate(s):
            if i != len(s) - 1:
                if char == "I" and (s[i + 1] != "V" or s[i + 1] != "X"):
                    sol -= numerals[char]
                elif char == "X" and (s[i + 1] != "L" or s[i + 1] != "C"):
                    sol -= numerals[char]
                elif char == "C" and (s[i + 1] != "D" or s[i + 1] != "M"):
                    sol -= numerals[char]
                else:
                    sol += numerals[char]
            else:
                sol += numerals[char]
        return sol