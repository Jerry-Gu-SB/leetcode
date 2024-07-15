class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # brute force:
        # check every single subset, sum it against its opposite
        # NOT SUBSET, PERMUTATION
        # DID THE TREE, STARTING TO UNDERSTAND SOMETHING. LET ME COOK TOMORROW.
        half = sum(nums) / 2
        print(sum(nums))
        print(half)

        for i in range(len(nums) + 1):
            for j in range(i + 1, len(nums) + 1):
                print(nums[i: j], sum(nums[i: j]))
                if sum(nums[i: j]) == half:
                    return True
        return False