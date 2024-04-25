class Solution:
    def longestIdealString(self, s: str, k: int) -> int:
        dp = [0] * 26
        for c in s:
            m = 1
            cur = ord(c) - ord('a')
            for i in range(26):
                if abs(cur - i) <= k:
                    m = max(m, dp[i]+1)
            dp[cur] = max(m, dp[cur])
        return max(dp)