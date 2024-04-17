# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if node == None:
                return 0
            print("node value: " + str(node.val))
            print(dfs(node.left), dfs(node.right))
            return max(dfs(node.left) + 1, dfs(node.right) + 1)
        if root.left and not root.right:
            return dfs(root.left)
        elif not root.left and root.right:
            return dfs(root.right)
        elif not root.right and not root.left:
            return 0
        else:
            return dfs(root)