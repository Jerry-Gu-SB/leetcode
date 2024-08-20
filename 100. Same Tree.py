# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # has to just be an O(n) algo just BFSing through
        if (p != None) ^ (q != None):
            return False
        if (p == None) and (q == None):
            return True

        p_queue = [p]
        q_queue = [q]
        while p_queue:
            p_cur = p_queue.pop(0)
            q_cur = q_queue.pop(0)

            if p_cur.val != q_cur.val or (p_cur.right != None) ^ (q_cur.right != None) or (p_cur.left != None) ^ (
                    q_cur.left != None):
                return False

            if p_cur.right:
                p_queue.append(p_cur.right)
                q_queue.append(q_cur.right)
            if p_cur.left:
                p_queue.append(p_cur.left)
                q_queue.append(q_cur.left)
        return True