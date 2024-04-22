class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        def overlaps(checked_interval, new_interval):
            # overlapping cases:
            #   1. fully in between
            #   2. new interval goes over
            #   3. new interval goes under
            if checked_interval[0] <= new_interval[0] <= checked_interval[1] or checked_interval[0] <= new_interval[
                1] <= checked_interval[1]:
                return True
            else:
                return False

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

        in_between = False
        subseq_interval = False
        solution = []
        temp_interval = [float("inf"), float("-inf")]
        for cur_interval in intervals:
            if in_between:
                solution.append(cur_interval)
                continue

            if not overlaps(cur_interval, newInterval):
                if subseq_interval and newInterval[0] > cur_interval[1]:
                    solution.append(temp_interval)
                    solution.append(cur_interval)
                    in_between = True
                elif subseq_interval:
                    solution.append(temp_interval)
                    solution.append(cur_interval)
                    in_between = True
                else:
                    solution.append(cur_interval)
            else:
                temp_interval[0] = min(cur_interval[0], newInterval[0], temp_interval[0])
                temp_interval[1] = max(cur_interval[1], newInterval[1], temp_interval[1])
                subseq_interval = True

        if not subseq_interval or not in_between:
            if newInterval[1] < intervals[0][0]:
                intervals.insert(0, newInterval)
                return intervals
            elif newInterval[0] > intervals[-1][1]:
                intervals.append(newInterval)
                return invertals
        return solution
