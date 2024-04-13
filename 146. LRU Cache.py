# have a dictionary for the constant retrievals
# check dictionary length with just len(dic.keys())
# track least recently used with a queue. if you use a key, then move the key to the back
# if a key is evicted, then remove from dictionary, and then remove from queue.
# LRUCache initialization is just setting the global size variable and instantiating the dictionary
from collections import defaultdict


class LRUCache:

    def __init__(self, capacity: int):
        self.length = capacity
        self.dict = defaultdict(int)
        self.LRU = []

    def get(self, key: int) -> int:
        if key in self.dict:
            self.LRU.pop(key)
            self.LRU.append(key)
            return key

    def put(self, key: int, value: int) -> None:

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)