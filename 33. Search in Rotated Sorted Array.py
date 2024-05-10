class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # have to modify binary search in a way that it can go both ways
        # the only thing i can think of is doing 2 binary searches for both sections
        # just breaking it in half each time, but that's really just doing a linear search isn't it..

        # note that the last digit is alwasy going to be the max of either the whole
        # thing or the pivited section. so you can check that to see if there's a pivot
        # in the first place, OR you can do your binary search inside there.