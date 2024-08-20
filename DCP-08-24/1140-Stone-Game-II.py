class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        n = len(piles)

        @cache
        def dp(l, M=1):
            min_stones = left_stones = sum(piles[l:])
            
            R = min(l + 2*M, n) + 1
            for r in range(l+1, R):
                stones = dp(r, max(M, r - l))
                min_stones = min(min_stones, stones)
            
            return left_stones - min_stones

        return dp(0)
