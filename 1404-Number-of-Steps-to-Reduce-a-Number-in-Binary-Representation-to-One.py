class Solution:
    def numSteps(self, s: str) -> int:
        s = int(s, 2)
        count = 0
        while s != 1:
            if (s & 1) == 0: # even
                s = s >> 1
            else:
                s = -(~s)
            count+=1
        return count