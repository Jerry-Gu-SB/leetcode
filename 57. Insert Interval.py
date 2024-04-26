class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals: return [newInterval]

        def overlaps(checked_interval, new_interval):
            # overlapping cases:
            #   1. other interval fully in between
            #   2. new interval goes over
            #   3. new interval goes under
            if checked_interval[0] <= new_interval[0] <= checked_interval[1] or checked_interval[0] <= new_interval[
                1] <= checked_interval[1] or (
                    checked_interval[0] >= new_interval[0] and checked_interval[1] <= new_interval[1]):
                return True
            else:
                return False

        if newInterval[1] < intervals[0][0]:
            intervals.insert(0, newInterval)
            return intervals
        elif newInterval[0] > intervals[-1][1]:
            intervals.append(newInterval)
            return intervals

        solution = []
        overlapped = False
        has_overlapped = False
        new_interval_inserted = False
        temp_interval = [float('inf'), float('-inf')]
        for i, cur_interval in enumerate(intervals):
            if overlaps(cur_interval, newInterval):
                temp_interval[0] = min(cur_interval[0], newInterval[0], temp_interval[0])
                temp_interval[1] = max(cur_interval[1], newInterval[1], temp_interval[1])
                overlapped = True
                if (i == len(intervals) - 1):
                    solution.append(temp_interval)
            else:
                if overlapped:
                    solution.append(temp_interval)
                    overlapped = False
                    has_overlapped = True
                elif not has_overlapped and newInterval[1] < cur_interval[0] and not new_interval_inserted:
                    solution.append(newInterval)
                    new_interval_inserted = True
                solution.append(cur_interval)

        return solution

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

        # if len(intervals) == 1:
        #     if overlaps(intervals[0], newInterval):
        #         temp = intervals[0]
        #         return [min(temp[0], newInterval[0]), max(temp[1], newInterval[1])]
        #     else:
        #         if newInterval[1] < intervals[0][0]:
        #             intervals.insert(0, newInterval)
        #             return intervals
        #         elif newInterval[0] > intervals[-1][1]:
        #             intervals.append(newInterval)
        #             return invertals

        # in_between = False
        # subseq_interval = False
        # solution = []
        # temp_interval = [float("inf"), float("-inf")]
        # for cur_interval in intervals:
        #     print(cur_interval)
        #     if in_between:
        #         print("IN_BETWEEN")
        #         solution.append(cur_interval)
        #         continue

        #     if not overlaps(cur_interval, newInterval):
        #         print("NOT OVERLAP")
        #         # if subseq_interval and newInterval[0] > cur_interval[1]:
        #         #     solution.append(temp_interval)
        #         #     solution.append(cur_interval)
        #         #     in_between = True
        #         if subseq_interval:
        #             print("subsequent interval")
        #             solution.append(temp_interval)
        #             solution.append(cur_interval)
        #         else:
        #             print("not sub interval")
        #             solution.append(cur_interval)
        #     else:

        #         temp_interval[0] = min(cur_interval[0], newInterval[0], temp_interval[0])
        #         temp_interval[1] = max(cur_interval[1], newInterval[1], temp_interval[1])
        #         subseq_interval = True
        #         print("should be just merging intervals: ", temp_interval)

        # if not subseq_interval or not in_between:
        #     if newInterval[1] < intervals[0][0]:
        #         intervals.insert(0, newInterval)
        #         return intervals
        #     elif newInterval[0] > intervals[-1][1]:
        #         intervals.append(newInterval)
        #         return invertals

        # if not solution: return temp_interval
        # return solution
