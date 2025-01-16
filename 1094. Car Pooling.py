class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        # It'd be nice if i could sort the lists by the START, and then I could naively
        # just iterate through and simulate the car. I think I'd like to try that off first

        # or I think you can just have a timeline like a list of each trip, and you
        # can just update each time in the list

        timeline = []
        for trip in trips:
            passengers = trip[0]
            start = trip[1]
            destination = trip[2]

            # extend the timeline as needed
            while len(timeline) < destination:
                timeline.append(0)
            for i in range(start, destination):
                timeline[i] += passengers
                if timeline[i] > capacity:
                    return False

        return True
