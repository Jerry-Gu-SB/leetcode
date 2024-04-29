class MinStack:
    # probably just use a stack and a minheap. wait but you'd have to take away the minheap too.
    # mmmm you can just have a dictionary of the current min for each value inserted.
    def __init__(self):
        self.stack = []
        self.min_dict = {}
        self.cur_min = float("inf")
    def push(self, val: int) -> None:
        self.stack.append(val)
        self.cur_min = min(self.cur_min, val)
        self.min_dict[len(self.stack)] = self.cur_min

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_dict[len(self.stack)]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()