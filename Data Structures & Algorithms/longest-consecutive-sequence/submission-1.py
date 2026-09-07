class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """
        Hash set ver: 
        - Iterate from the beginning of list, check if the expected next num exist
        - Use an adder to store the streak and... Similar to s1.
        """
        numset = set(nums)
        res = 0

        for num in numset:
            
            if (num - 1) not in numset:     # How to locate the starter of a seq
                streak = 1

                while (num + streak) in numset:
                    streak += 1

                res= max(streak, res)

        return res