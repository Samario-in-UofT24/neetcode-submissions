class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        """
        With the use of Sorting, it is easy to get the duplicate

        O(nlogn) for time
        """
        nums.sort()
        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                return nums[i]
        return -1