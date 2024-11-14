class Solution:
    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:
        def can_dist(x):
            s = 0
            for q in quantities:
                s += ceil(q / x)
            return s > n
        l, r = 1, 100000
        while r >= l:
            m = (r+l) // 2
            if can_dist(m):
                l = m+1
            else:
                r = m - 1

        return l