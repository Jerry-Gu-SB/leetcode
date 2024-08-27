# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # is there a way where the greedy also breaks?
        # i dont hink so
        # wiat i'm dumb you can do it if the right brancha dn left branch have in between vals
        # track the minimum value you've run into as you DFS through the tree i think
        # need to figure out how to track it as we backtrack?
        # well if we start from the root then it works?? if i write the recursion properly...
        if not root:
            return False



