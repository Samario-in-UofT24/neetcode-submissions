# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        """
        From bottom to top, with recursion

        Just like making up a Heap, the diff between the two methods
        """
        def recur_to_bot(root):

            if not root:    # Empty scenario
                return [True, 0]    # [if subtree balanced, height of the root]

            # common scenarios
            left = recur_to_bot(root.left)
            right = recur_to_bot(root.right)

            balanced = left[0] and right[0] and abs(left[1] - right[1]) <= 1

            return [balanced, 1 + max(left[1], right[1])]
        
        return recur_to_bot(root)[0]
            