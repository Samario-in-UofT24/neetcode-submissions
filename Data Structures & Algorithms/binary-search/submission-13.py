class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
        Most basic BS with sorted arr
        """
        left = 0
        right = len(nums) - 1

        while left <= right:

            mid = ( left + right ) // 2

            if nums[mid] == target:
                return mid

            elif nums[mid] < target:
                left = mid + 1

            else:
                right = mid - 1

        return -1