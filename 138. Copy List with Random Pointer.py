"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""


class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # so ideally if I were doign this, I would just have an array of a preset length, and then as I go to each next node, I just know which one slots in where in the array.
        # think 2 passes should do the trick
        # pass 1: initialize array with empty nodes
        # pass 2: just uhhh set the values i guess?

        # pass 1:
        list_len = 0
        list_array = []
        dicto = {}

        temp = head
        while temp:
            dicto[temp] = list_len
            empty_node = Node(0, None, None)
            list_array.append(empty_node)

            temp = temp.next
            list_len += 1

        list_array.append(None)

        # pass 2:
        for i in range(list_len):
            cur_node = list_array[i]

            cur_node.val = head.val
            cur_node.next = list_array[i + 1]

            if head.random:
                cur_node.random = list_array[dicto[head.random]]
            else:
                cur_node.random = list_array[list_len]

            head = head.next

        return list_array[0]
