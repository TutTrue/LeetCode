class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        memo = {}
        def rec(r, c, M):
            if (r, c, M) in memo: return memo[(r, c, M)]
            if r < 0 or c < 0 or r >= m or c >= n: return 1
            if M == 0: return 0

            ans = 0
            ans+=rec(r+1, c, M-1)
            ans+=rec(r, c+1, M-1)
            ans+=rec(r, c-1, M-1)
            ans+=rec(r-1, c, M-1)
            memo[(r, c, M)] = ans
            return ans
        return rec(startRow, startColumn, maxMove) % (10**9+7)
        