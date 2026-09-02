class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        """
        - Is the answer one of the num in piles ?

        With Hint 1:
            x: amount of one pile 
            r: rate of eating
            need ceiling(x/r) to finish this pile
        With Hint 2:
            num_of_pile = len(piles)
            h >= num_of_pile
            total bananas <= maxima in piles * num_of_pile
            r * h >= total bananas
            upper bound of r: maxima in piles

        Then lower bound of r: 1
        """
        l = 1
        r = max(piles)
        res = r

        while l <= r:
            m = (l + r) // 2

            time = 0
            for p in piles:
                time += math.ceil(float(p) / m)
            if time <= h:
                res = m
                r = m - 1

            else:
                l = m + 1

        return res