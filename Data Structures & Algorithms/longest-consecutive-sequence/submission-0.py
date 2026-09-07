class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """
        Strategy of refreshing the result:
            Def a var to store the res
            Def another var for specific scenario(maybe in a loop), set an optional update
                E.g. max(res, optinal update)

        Sort based: absolutely O(nlogn)
        - Sorting gathers the consecutive together
        """
        if not nums:
            return 0

        res = 0
        nums.sort()

        curr = nums[0]
        streak = 0  # temp_adder
        i = 0

        while i < len(nums):
            # Moves to another seq, re-initialize
            if curr != nums[i]:
                curr = nums[i]
                streak = 0

            while i < len(nums) and curr == nums[i]:
                # Q: Why while-loop? 
                # A: To skip the duplicates and move the i to front of new num
                i += 1

            streak += 1 
            curr += 1   # The next number expected to exist

            res = max(res, streak)
            
            # Q: Why the i is not updated here again
            # A: updated in block above
        return res

