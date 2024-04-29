class Solution:
    from collections import deque
    def evalRPN(self, tokens: List[str]) -> int:
        # use stack.
        # just initilize as a deque to get O(1) pops and insertions
        # then just switch statement for +/-*
        # if an operation pop the next two items and do the operation
        # if number, toss on the stack

        stack = deque()

        for token in tokens:
            if token == '+':
                first = stack.pop()
                second = stack.pop()
                stack.append(first + second)
            elif token == '*':
                first = stack.pop()
                second = stack.pop()
                stack.append(first * second)
            elif token == '/':
                first = stack.pop()
                second = stack.pop()
                stack.append(int(second / first))
            elif token == '-':
                first = stack.pop()
                second = stack.pop()
                stack.append(second - first)
            else:
                stack.append(int(token))
        return int(stack[0])