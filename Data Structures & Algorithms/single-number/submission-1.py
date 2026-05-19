class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        """
        First thought:
        - Create a dict {num: time}
        - Update it during iteration of list
        - Then iterate the dict, if time is 1, return it

        """
        temp = {}

        for num in nums:
            if num in temp:
                temp[num] += 1
            else:
                temp[num] = 1
        
        for num in temp:
            if temp[num] == 1:
                return num