class Solution:
    def numTeams(self, rating: List[int]) -> int:
        res = 0
        N = len(rating)
        for m in range(N):
            l = r = 0
            for i in range(m):
                if rating[i] < rating[m]:
                    l += 1
            for i in range(m + 1, N):
                if rating[i] > rating[m]:
                    r += 1
            res += l*r
            res += (N - m - 1 - r) * (m - l)
        return res
