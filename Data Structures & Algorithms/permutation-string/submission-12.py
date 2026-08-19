class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        """
        The core is the "Sliding window" in s2
        But this is not yet real sliding window but to get a subpart by slicing.

        Use the dict to solve this
        """
        count1 = {}
        for c in s1:
            count1[c] = 1 + count1.get(c, 0)

        need = len(count1)  # char and corresponding number needed

        for i in range(len(s2)):    # Set the start and initialize c2
            count2, cur = {}, 0

            for j in range(i, len(s2)):
                count2[s2[j]] = 1 + count2.get(s2[j], 0) # update val

                if count1.get(s2[j], 0) < count2[s2[j]]:
                    break
                if count1.get(s2[j], 0) == count2[s2[j]]:
                    cur += 1
                if cur == need:
                    return True
        return False