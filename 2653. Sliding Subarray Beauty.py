class Solution:
    def getSubarrayBeauty(self, nums: List[int], k: int, x: int) -> List[int]:
        # slidign window i guess
        # put zero in the array if there's fewer than x negative integers

        # xth smallest integer is the problem i think unless you use a heap or something?

        # naive way, need to speed this jit up.
        # start = 0
        # end = k
        # solution = []
        # while end <= len(nums):
        #     heap = []
        #     heapify(heap)
        #     negatives = 0
        #     for i in range(start, end):
        #         heappush(heap, nums[i])
        #         if nums[i] < 0:
        #             negatives += 1
        #     if negatives >= x:
        #         solution.append(nsmallest(x, heap)[-1])
        #     else:
        #         solution.append(0)
        #     start += 1
        #     end += 1
        # return solution

        listo = []
        for num in range(0, 50):
            listo.append(0)

        negatives = 0
        for i in range(k):
            if nums[i] < 0:
                negatives += 1
                listo[nums[i] + 50] += 1

        solution = []
        start = 0
        end = k - 1
        while end < len(nums):
            counter = 0
            if negatives >= x:
                for i, num in enumerate(listo):
                    counter += num
                    if counter >= x:
                        solution.append(i - 50)
                        break
            else:
                solution.append(0)

            if nums[start] < 0:
                listo[nums[start]] -= 1
                negatives -= 1

            start += 1
            end += 1
            if end < len(nums) and nums[end] < 0:
                listo[nums[end]] += 1
                negatives += 1

        return solution

