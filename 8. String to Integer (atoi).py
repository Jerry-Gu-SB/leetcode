class Solution:
    def myAtoi(self, s: str) -> int:
        state = 0
        value = 0  # should be named solution i think
        pos = 0  # honestly should be named pointer or index or i or something liek that
        sign = 1  # a better implementation of my negative boolean i think

        if len(s) == 0: return 0

        while pos < len(s):

            cur = s[pos]

            if state == 0:
                if cur == " ":
                    state = 0
                elif cur == "+" or cur == "-":
                    state = 1
                    if cur == "+":
                        sign = 1
                    else:
                        sign = -1

                elif cur.isdigit():
                    state = 2
                    # just adding the digits mathematically instead of by a string

                    # HONESTLY I could just add chars to a string here since
                    # we don't do math to it except here and when we multiply the sign
                    # but we can just add chars, convert at the end, then multiply
                    # but i'm unsure whether this is faster.
                    # either way i think it's cooler, but maybe less readable.
                    value = value * 10 + int(cur)
                else:
                    return 0

            elif state == 1:
                if cur.isdigit():
                    state = 2
                    # just adding the digits mathematically instead of by a string
                    value = value * 10 + int(cur)
                else:
                    return 0  # invalid string, return 0 to escape DFA

            elif state == 2:
                if cur.isdigit():
                    # just adding the digits mathematically instead of by a string
                    value = value * 10 + int(cur)
                else:
                    break
            else:
                return 0  # left the state machine
            pos += 1  # read next character

        # if added digits string wise, just convert here to int, then do value multiply.
        value *= sign  # sign will be 1 or -1

        # bounds check
        value = min(value, 2 ** 31 - 1)
        value = max(-(2 ** 31), value)

        return value
        # does it step by step this way by just implementing the algorithm,
        # but a cooler way to do it is to use a finite state machine or deterministic finite automata
#         if len(s) == 0: return 0
# # Whitespace: Ignore any leading whitespace (" ").
#         s = s.strip()
#         if len(s) == 0: return 0
# # Signedness: Determine the sign by checking if the next character is '-' or '+',
# # assuming positivity is neither present.
#         negative = False
#         if s[0] == '-':
#             negative = True
#             s = s[1::]
#         elif s[0] == '+':
#             negative = False
#             s = s[1::]
#         else:  # not really necessary but whatever
#             negative = False
#         if len(s) == 0: return 0
# # Conversion: Read the integer by skipping leading zeros until a non-digit character is
# # encountered or the end of the string is reached. If no digits were read, then the result is 0.

#         # skip leading zeroes
#         while s[0] == '0':
#             s = s[1:]
#             if len(s) == 0: return 0

#         # read digits until the end of string or non-digit read
#         for i, char in enumerate(s):
#             if not char.isdigit():
#                 s = s[:i]  # exclude current character
#                 break
#         if len(s) == 0: return 0

# # Rounding: If the integer is out of the 32-bit signed integer range [-231, 231 - 1],
# # then round the integer to remain in the range. Specifically, integers less than -231
# # should be rounded to -231, and integers greater than 231 - 1 should be rounded to 231 - 1
#         print("s: ", s, "int(s) ", int(s))
#         s = int(s)

#         if negative: s *= -1

#         if s < -2**31:
#             s = -2**31
#         elif s > 2**31 - 1:
#             s = 2**31 - 1

#         return s
