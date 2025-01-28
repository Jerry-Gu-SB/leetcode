# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque


class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        # cooler way of doing it: https://www.youtube.com/watch?v=ufoXtgrK86o

        # i think you just BFS to find the target while tracking the levels. once you find the target node, you can just add all the nodes in the queue that you were about to add
        # OR alternatively, you can just reconstruct the entire graph in an O(n) space way and then just run a single BFS on that without it b eing a binary graph. I feel liek SURELY there's a way we can abuse the fact that the grpah is binary though

        # first BFS:

        # visited = set()
        # queue

        # WAIT A SEC, you can just track the nodes at each level. just keep a list of every node at every level. on. just kidding i dont t hink this actualy works unless you're trackign which side the node is on.

        # like okay, you could just recreate the entire tree and make it undirected and then it'd work i guess??

        # so keep track of your path till you get to the target
        # once you get to the target, backtrack through that path and BFS to find all the targets on the other side at depth:(k - distance from target)

        graph = {}
        graph_target = None
        queue = deque()
        visited = set()
        queue.append(root)
        while queue:
            cur = queue.popleft()
            if cur == target:
                graph_target = cur.val
            if cur not in visited:
                if cur.val not in graph.keys():
                    graph[cur.val] = []

                if cur.left:
                    graph[cur.val].append(cur.left.val)
                    graph[cur.left.val] = [cur.val]
                    queue.append(cur.left)

                if cur.right:
                    graph[cur.val].append(cur.right.val)
                    graph[cur.right.val] = [cur.val]
                    queue.append(cur.right)

                visited.add(cur)
        # print("graph:", graph)
        # print("graph_target", graph_target)

        # bfs
        queue = deque()
        visited = set()
        queue.append([graph_target, k])

        solution = []
        while queue:
            cur, cur_k = queue.popleft()
            if cur_k == 0:
                solution.append(cur)

            if cur not in visited:
                for node in graph[cur]:
                    if node not in visited:
                        queue.append([node, cur_k - 1])
                visited.add(cur)
        # print("visited:", visited)
        # print("solution:", solution)
        return solution