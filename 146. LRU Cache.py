# have a dictionary for the constant retrievals
# check dictionary length with just len(dic.keys())
# track least recently used with a queue. if you use a key, then move the key to the back
# if a key is evicted, then remove from dictionary, and then remove from queue.
# LRUCache initialization is just setting the global size variable and instantiating the dictionary
# THIS IS SLOW BECAUSE REMOVE() RUNS IN LINEAR TIME
from collections import defaultdict


class LRUCache:

    def __init__(self, capacity: int):
        self.length = capacity
        self.dict = defaultdict(int)
        self.LRU = []

    def get(self, key: int) -> int:
        if key in self.dict:
            self.LRU.remove(key)
            self.LRU.append(key)
            return self.dict[key]
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.dict:
            self.LRU.remove(key)
            self.LRU.append(key)
            self.dict[key] = value
        else:
            if len(self.LRU) == self.length:
                del self.dict[self.LRU[0]]
                del self.LRU[0]
            self.dict[key] = value
            self.LRU.append(key)

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)