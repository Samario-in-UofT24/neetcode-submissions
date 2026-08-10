class Solution:
    def countBits(self, n: int) -> List[int]:
        """
        Question:
            - How to get the num of "1" for a given num's binary repre?
        Answer:
            - Bit masking. 
            * The integer(int) in python is trated as binary number        
        """
        res = []

        # range [0,n]
        for num in range(n + 1):
            temp = 0

            # assume stored in 32 bits
            for i in range(32):
                if num & (1 << i):
                    temp += 1
            res.append(temp)

        return res