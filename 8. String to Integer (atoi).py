class Solution:
    def myAtoi(self, s: str) -> int:

        if len(s) == 0: return 0
        # Whitespace: Ignore any leading whitespace (" ").
        s = s.strip()
        if len(s) == 0: return 0
        # Signedness: Determine the sign by checking if the next character is '-' or '+',
        # assuming positivity is neither present.
        negative = False
        if s[0] == '-':
            negative = True
            s = s[1::]
        elif s[0] == '+':
            negative = False
            s = s[1::]
        else:  # not really necessary but whatever
            negative = False
        if len(s) == 0: return 0
        # Conversion: Read the integer by skipping leading zeros until a non-digit character is
        # encountered or the end of the string is reached. If no digits were read, then the result is 0.

        # skip leading zeroes
        while s[0] == '0':
            s = s[1:]
            if len(s) == 0: return 0

        # read digits until the end of string or non-digit read
        for i, char in enumerate(s):
            if not char.isdigit():
                s = s[:i]  # exclude current character
                break
        if len(s) == 0: return 0

        # Rounding: If the integer is out of the 32-bit signed integer range [-231, 231 - 1],
        # then round the integer to remain in the range. Specifically, integers less than -231
        # should be rounded to -231, and integers greater than 231 - 1 should be rounded to 231 - 1
        print("s: ", s, "int(s) ", int(s))
        s = int(s)

        if negative: s *= -1

        if s < -2 ** 31:
            s = -2 ** 31
        elif s > 2 ** 31 - 1:
            s = 2 ** 31 - 1

        return s
