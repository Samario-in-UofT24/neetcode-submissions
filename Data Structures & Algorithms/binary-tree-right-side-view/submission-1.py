# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        """
        First thought:
        - Use BFS from the root
        - Use a hash table with chaining, the node.d as key
        - Then just return the right-most key of the chain

        Second thought:
        - Imitate the "Level Order Traversal" question, append the last val in the lvl to res
        - A better way is just keep updating the val so it stops at the end
        """
        res = []
        q = collections.deque()

        q.append(root)

        while q:
            rightMost = None

            for i in range(len(q)):
                node = q.popleft()
                if node:
                    rightMost = node.val
                    q.append(node.left)
                    q.append(node.right)

            if rightMost:
                res.append(rightMost)

        return res


