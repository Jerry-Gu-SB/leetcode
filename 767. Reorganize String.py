class Solution:
    def reorganizeString(self, s: str) -> str:
        # I think you should probably do this with a counter, then just start alternating the most occuring letters at a time in a greedy fashion?
        # if len(s) == 1: return s

        # count = Counter(s)

        # for key in count.keys():
        #     if count[key] > (len(s) + 1) // 2:
        #         return ""

        # sorted_dict = sorted(count.items(), key=lambda kv: (kv[1], kv[0]), reverse=True)
        # for i in range(len(sorted_dict)):
        #     sorted_dict[i] = list(sorted_dict[i])

        # print(sorted_dict)
        # left = 0
        # right = 1

        # right_flag = False

        # solution = ""

        # while len(solution) < len(s):
        #     print("left:", left, "right:", right)
        #     print("sorted_dict:", sorted_dict)

        #     left_key = sorted_dict[left][0]
        #     left_value = sorted_dict[left][1]

        #     if left_value <= 0:
        #         left += 1
        #         print("-----LEFT CONTINUE")
        #         continue
        #     if not right_flag or right >= len(s) - 1:
        #         solution += left_key
        #         sorted_dict[left][1] -= 1
        #     else:
        #         right_flag = False

        #     if right >= len(s) - 1:
        #         continue
        #     right_key = sorted_dict[right][0]
        #     right_value = sorted_dict[right][1]
        #     if right_value <= 0 or left == right:
        #         right += 1
        #         right_flag = True
        #         print("-----RIGHT CONTINUE")
        #         continue

        #     solution += right_key
        #     sorted_dict[right][1] -= 1

        #     print("left_key:", left_key, "right_key", right_key)

        #     print("solution:", solution)
        # return solution

        # yeah this is clearly and obviouslynot how you shoudl go about doing this. let's check out the answer

        # NeetCode:
        # you had the same approach, but you didn't understand the key point where instead of doing all this weird 2 pointer stuff across a hashmap, you can just track the previous value. Ultimately, that's the only rule, so we're just encoding that rule.
        # I think your idea is solid, but you just missed an easier way to track the things
        # also start using heaps more if you need to keep resorting values in an edited list.
        count = Counter(s)
        res = ""

        heap = [[-val, key] for key, val in count.items()]  # this is how you make a heap
        heapq.heapify(heap)  # remember sorting like this. this will be very very helpful in the future.
        prev = None

        while heap or prev:
            # this basicaly only happens when we just have 1 letter left that has more stuff to do, but we just put that same letter in the solution
            if not heap and prev:
                return ""

            cur_val, cur_char = heapq.heappop(heap)  # grab the most common value
            res += cur_char  # attach it to the solution
            cur_val += 1  # increment as it's negative for a min heap of negative nums

            # if there's a previous value, we just put it back onto the heap so that way we can use it again
            if prev:
                heapq.heappush(heap, prev)
                prev = None  # reset it. that way in the next line, we'll know we're done if prevoius isn't set
            if cur_val != 0:
                prev = [cur_val,
                        cur_char]  # this is because here prev is only set if we still need to add on some values

        return res

