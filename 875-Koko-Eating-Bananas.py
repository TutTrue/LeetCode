class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        while l <= r:
            m = (l+r)//2
            hour = 0
            for j in piles:
                hour += ceil(j / m)
            if hour <= h:
                r = m-1
            else:
                l = m+1
        return l