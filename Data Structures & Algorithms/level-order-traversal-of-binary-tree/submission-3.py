# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        """
        BFS? THe nested list is the nodes with same node.d

        Revisit BFS:
        - Use of Queue to store the Grey nodes
        - Enqueue the root as the start
        
        The modified part for this BFS:
        - **The queue stores the nodes in next level at a time**
        - Then dequeue the num of the nodes in next round, not one by one

        """
        res = []

        # Initialize the BFS
        q = collections.deque()
        q.append(root)

        while q:
            lvl = []    # To store the answer 

            for i in range(len(q)):
                node = q.popleft()

                if node:
                    q.append(node.left)
                    q.append(node.right)
                    lvl.append(node.val)

            if lvl:
                res.append(lvl)

        return res

