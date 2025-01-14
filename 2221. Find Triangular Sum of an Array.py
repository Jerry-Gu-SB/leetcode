class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        # naive
        cur_list = nums
        while len(cur_list) > 1:
            new_list = []
            for i in range(len(cur_list) - 1):
                new_list.append((cur_list[i] + cur_list[i + 1]) % 10)
            cur_list = new_list
        return cur_list[0]

        # okay so essentially the optimized linear time solution is some insane math thing with pascals triangle

        # https://leetcode.com/problems/find-triangular-sum-of-an-array/solutions/1907380/o-n-time-o-1-space-python-189-ms-c-12-ms-java-4-ms