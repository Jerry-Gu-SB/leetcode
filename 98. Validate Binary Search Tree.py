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
        # track 15the minimum value you've run into as you DFS through the tree i think
        # need to figure out how to track it as we backtrack?
        # well if we start from the root then it works?? if i write the recursion properly...

        # in-order traversal: track the last left move, and the last right move, then you need to see the ranges from the last left and the last right. so for root root which has no last left or right, if you go left, then your range is ::root.val, and lastleft becomes root.val. if you go right, then the range is root.val:: and your last right becomes root.val.
        # so if go left, then go right, your value becomes cur.val::root.val, or making cur.val last right, lastright::lastleft. when i say lastright or lastleft, that refers to the left or right TURN, not the left or right VALUE.
        if not root:
            return False

        def recurse(range, node):
            sol = True
            if node:
                # First recur on left child
                sol = sol and recurse([range[0], node.val], node.left)

                # the recur on right child
                if not (range[0] < node.val < range[1]):
                    sol = False

                # now print the data of node
                sol = sol and recurse([node.val, range[1]], node.right)
            return sol

        return recurse([float('-inf'), float('inf')], root)



