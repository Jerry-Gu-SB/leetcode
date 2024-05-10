# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # it's just BFS. so have a global variable that goes down, and just add the index
        # list at that level i think
        if not root: return []
        solution = [[]]
        queue = [[root, 0]]
        # you actually dont need this, because you shouldn't visit the same place twice
        # yeah commenting this out literally changes nothing
        # visited = []
        while queue:
            # print(queue)
            cur = queue.pop(0)
            curNode = cur[0]
            if not curNode: continue
            curLevel = cur[1]
            while len(solution) <= curLevel:
                solution.append([])
            # if curNode not in visited:
            solution[curLevel].append(curNode.val)  # was originally tabbed in
            # visited.append(curNode)
            queue.append([curNode.left, curLevel + 1])
            queue.append([curNode.right, curLevel + 1])

        return solution

        # YEA NAH YOU GOOFY AF. just do the BFS algorithm you know with graphs, idk
        # you wnated to do a binary search tree dfs pattern, but that doesnt make
        # sense. you know how bfs works, just use that dog.
        # if not root: return []
        # solution = [[root.val]]

        # def dfs(node, level):
        #     global solution
        #     if level == 0: return 0
        #     solution[level + 1].append(dfs(node.left, level + 1))
        #     solution[level + 1].append(dfs(node.right, level + 1))
        #     print(solution)
        #     return node.val

        # dfs(root, 0)
        # print(solution)
        # return solution

