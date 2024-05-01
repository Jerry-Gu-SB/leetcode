from collections import defaultdict

#  this is the full implementation and bugfixing of my dictionary. there were some
# finnicky bits you had to fix, but should be lit now.
class MinStack:
    # probably just use a stack and a minheap. wait but you'd have to take away the minheap too.
    # mmmm you can just have a dictionary of the current min for each value inserted.
    def __init__(self):
        self.stack = []
        self.min_dict = defaultdict(int)

    def push(self, val: int) -> None:
        self.stack.append(val)
        if len(self.stack) > 1:
            val = min(val, self.min_dict[len(self.stack) - 1])
        self.min_dict[len(self.stack)] = val

    def pop(self) -> None:
        self.min_dict[len(self.stack)] = None
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


# this is the answer i took from the answers
# class MinStack:
#     # probably just use a stack and a minheap. wait but you'd have to take away the minheap too.
#     # mmmm you can just have a dictionary of the current min for each value inserted.
#     def __init__(self):
#         self.stack = []
#         self.min_stack = []
#
#     def push(self, val: int) -> None:
#         self.stack.append(val)
#         if self.min_stack:
#             val = min(self.min_stack[-1], val)
#         self.min_stack.append(val)
#
#     def pop(self) -> None:
#         self.stack.pop()
#         self.min_stack.pop()
#
#     def top(self) -> int:
#         return self.stack[-1]
#
#     def getMin(self) -> int:
#         return self.min_stack[-1]
#
# # Your MinStack object will be instantiated and called as such:
# # obj = MinStack()
# # obj.push(val)
# # obj.pop()
# # param_3 = obj.top()
# # param_4 = obj.getMin()