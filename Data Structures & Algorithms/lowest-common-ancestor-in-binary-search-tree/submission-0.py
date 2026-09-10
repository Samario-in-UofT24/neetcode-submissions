# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        """
        This is a BST

        The returned node.val must be greater or equal to p.val and smaller than q.val

        Traverse from the node to bottom

        Only change the answer to left/right when bigger/smaller than both p,q 
        Not equal
        """
        res = root

        while res:

            if p.val < res.val and q.val < res.val:
                res = res.left

            elif p.val > res.val and q.val > res.val:
                res = res.right

            else:
                return res