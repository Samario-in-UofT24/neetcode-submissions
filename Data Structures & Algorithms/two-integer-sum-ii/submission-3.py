class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        """
        Try to use the property of the given input: sorted
        """
        l, r = 0, len(numbers) - 1

        while l < r:
            curSum = numbers[l] + numbers[r]

            if curSum > target:
                r -= 1
            elif curSum < target:
                l += 1
            else:
                return [l + 1, r + 1]
        return []