class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        """
        Now consider: 
        During the traversal of the Temp List, using a stack to store 
        the day that haven't found a warmer day
        - directly append the traversed element into the stack

        Then if we found a warmer day, popping the element in the stack
        and calculate the "val"
        - with a while loop

        Remember to initialize a res list with 0 by default;
        Set the 0 with other "val" if conditions satisfied
        """
        res = [0] * len(temperatures)   # Initialization

        stack = []

        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][1]:   # Found a warmer day
                ind, temp = stack.pop()

                res[ind] = i - ind
            stack.append((i, t))

        return res
