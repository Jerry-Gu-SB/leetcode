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
        if not node: return None

        queue = deque([node])
        visited = {node.val: Node(node.val, [])}  # initializes dictionary typing

        while queue:
            cur = queue.popleft()
            cur_copy = visited[cur.val]

            for neighbor in cur.neighbors:
                if neighbor.val not in visited:
                    queue.append(neighbor)
                    visited[neighbor.val] = Node(neighbor.val, [])
                cur_copy.neighbors.append(visited[neighbor.val])
        return visited[node.val]