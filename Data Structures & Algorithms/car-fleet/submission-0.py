class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        """
        How can I keep track of so many cars as there is a change of speed?
        """
        pair = [(p, s) for p, s in zip(position, speed)]
        pair.sort(reverse=True)     # Reverse and sorted by pos

        stack = []

        for pos, spd in pair:  
            stack.append((target - pos) / spd)  # calc the "time"

            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
                
        return len(stack)

        