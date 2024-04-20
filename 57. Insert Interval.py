class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # iterate through intervals O(n)
        # if not overlapping: append to new interval list
        # else:
        #   the first interval that you encounter, create a new temp interval (don't insert)
        #   temp_interval initialize as [inf, -inf]
        #   temp_interval[0] = min(cur_interval, new_interval[0])
        #   set subsequent intervals flag
        #   for subsequent intervals, temp_interval[1] = max(cur_interval[1], new_interval[1], temp_interval[1])

        # edge cases: if new interval has no overlap. can be before, between, or after
            # before/after can be checked manually at the start
            # between has to be checked every iteration: current iterator doesn't overlap, new_int[0] > cur_int[1]

        def overlaps(checked_interval, new_interval):
            # overlapping cases:
            #   1. fully in between
            #   2. new interval goes over
            #   3. new interval goes under