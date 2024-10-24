class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        # hmmm not really quite sure what to think here
        # it would be nice if we coud linearly just swap each negative number to where it should be and then square, but i don't
        # really see how that's faster than nlogn
        # i'm having a hard time conceptualizing the sort in something faster than nlogn
        # maybe like put it in a heap or something??

        # fast, but not the right intuition or wha tinterviews woudl look for probably
        # h = []
        # for value in nums:
        #     heappush(h, value ** 2)
        # return [heappop(h) for i in range(len(h))]

        # 2 pointers, just iterate from both sides and sort them
        n = len(nums)
        ans = [0] * n
        start, end = 0, n - 1
        for i in range(n - 1, -1, -1):
            if abs(nums[start]) >= abs(nums[end]):
                ans[i] = nums[start] * nums[start]
                start += 1
            else:
                ans[i] = nums[end] * nums[end]
                end -= 1
        return ans
