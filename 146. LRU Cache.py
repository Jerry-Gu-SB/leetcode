# have a dictionary for the constant retrievals
# check dictionary length with just len(dic.keys())
# track least recently used with a queue. if you use a key, then move the key to the back
# if a key is evicted, then remove from dictionary, and then remove from queue.
# LRUCache initialization is just setting the global size variable and instantiating the dictionary
# THIS IS SLOW BECAUSE REMOVE() RUNS IN LINEAR TIME
class Node:
    def __init__(self, key=None, value=None, next=None, prev=None):
        self.key = key
        self.value = value
        self.next = next
        self.prev = prev


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0


class LRUCache:
    def __init__(self, capacity: int):
        LL = LinkedList()
        LL.head = Node()
        LL.tail = Node()
        LL.head.next = LL.tail
        LL.tail.prev = LL.head

        dicto = {}
        self.capacity = capacity

    def get(self, key: int) -> int:

    def put(self, key: int, value: int) -> None:
        if key in self.dicto:

        else:
            new_node = Node(key, value, LL.tail, LL.tail.prev)
            if self.capacity == LL.length:

            LL.tail.prev.next = new_node
            LL.tail.prev = new_node

        # from collections import defaultdict
# class LRUCache:

#     def __init__(self, capacity: int):
#         self.length = capacity
#         self.dict = defaultdict(int)
#         self.LRU = []

#     def get(self, key: int) -> int:
#         if key in self.dict:
#             self.LRU.remove(key)
#             self.LRU.append(key)
#             return self.dict[key]
#         else:
#             return -1


#     def put(self, key: int, value: int) -> None:
#         if key in self.dict:
#             self.LRU.remove(key)
#             self.LRU.append(key)
#             self.dict[key] = value
#         else:
#             if len(self.LRU) == self.length:
#                 del self.dict[self.LRU[0]]
#                 del self.LRU[0]
#             self.dict[key] = value
#             self.LRU.append(key)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)