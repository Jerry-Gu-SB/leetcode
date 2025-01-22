class Solution:
    def isPalindrome(self, x: int) -> bool:
        # surely there's a mathematical way to do this
        # if x < 0: return False
        # if x < 10: return True

        # stringo = str(x)

        # l = 0
        # r = len(stringo) - 1
        # while l < r:
        #     if stringo[r] == stringo[l]:
        #         l += 1
        #         r -= 1
        #     else:
        #         return False
        # return True

        # fun math way to solve it
        if x < 0:
            return False

        reverse = 0
        xcopy = x

        while x > 0:
            reverse = (reverse * 10) + (x % 10)
            x //= 10

        return reverse == xcopy