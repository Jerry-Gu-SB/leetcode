"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
from collections import defaultdict


class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # just kinda looks like a BFS

        # okay yeah it's a BFS, i messed up the typing. you need ot actually return the
        # CLONE of the original node. it means likke actually clone and make new nodes
        # seems annoying. just use the values to check the queue visited, then return
        # cloned nodes
        if not node: return []
        if not node.neighbors: return [[]]
        queue = [node]
        adjacency = defaultdict(list)
        visited = []
        while queue:
            cur = queue.pop(0)
            cur = Node(cur.val)
            if cur.val not in visited:
                visited.append(cur.val)

                if not cur.neighbors: continue

                for neighbor in cur.neighbors:
                    neighbor = Node(neighbor.val)
                    if neighbor.val not in visited:
                        queue.append(neighbor.val)
                    adjacency[cur].append(neighbor)
        print(adjacency)
        # solution = []
        # for key in adjacency.keys():
        #     print("key: ", key)
        #     print("key values: ", adjacency[key])
        #     while len(solution) < key:
        #         solution.append([])
        #     for val in adjacency[key]:
        #         solution[key - 1].append(val)
        # print(solution)
        return adjacency[node]





