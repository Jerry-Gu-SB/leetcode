class Solution:
    def trap(self, height: List[int]) -> int:
        # possible variations
        # small -> big
        # big -> small
        # borders (nothing)
        # same -> same

        # if you have something right next to it, then you know it can't trap anything

        # BUT YOU CAN'T KNOW WHICH IS THE BIGGEST I THINK

        # i think maybe you need to start from the tallest, and go layer by layer?
        # then you just look for anything the same or taller, and count that layer.
        # SO HOW DO YOU CAPTURE BIG -> SMALL?
        # you can just count bigger things as that layer i think. so a 2 tall building is the same as a 1 tall, and you're just capturing 1 layer at a time anyway.

        solution = 0
        ordered_list = sorted(list(set(height)), reverse=True)

        for max_height in ordered_list:
            print("----------max_height:", max_height)
            last_seen = None
            for i, column in enumerate(height):
                print("last_seen", last_seen, "column:", column)

                if column >= max_height and last_seen and i - last_seen > 1:
                    print("adding solution!", i - last_seen - 1)
                    solution += i - last_seen
                    last_seen = i
                if column >= max_height:
                    last_seen = i
            print("cur_solution", solution)
        return solution



