class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        """
        BST in two-dimensions:

        - Use BST to locate the row 
        - Then inside the row, with BST again to find the target
        """
        m, n = len(matrix), len(matrix[0])

        top = 0
        bot = m - 1

        while top <= bot:
            mid = (top + bot) // 2
            rowi = mid
            if target > matrix[rowi][-1]:
                top = rowi + 1
            elif target < matrix[rowi][0]:
                bot = rowi - 1
            else:
                break   # finish the search for row, exit the loop

        if not (top <= bot):    # Yes it can be <, consider many duplicates scenario
            return False

        # express the located row here
        row = (top + bot) // 2     # Check scenarios with many duplicates
        l, r = 0, n - 1
        
        while l <= r:
            m = (l + r) // 2

            if target > matrix[row][m]:
                l = m + 1

            elif target < matrix[row][m]:
                r = m - 1

            else:
                return True

        return False        