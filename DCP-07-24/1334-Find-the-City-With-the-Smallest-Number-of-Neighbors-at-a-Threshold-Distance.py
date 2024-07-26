class Solution:
    def findTheCity(
        self, n: int, edges: List[List[int]], distanceThreshold: int
    ) -> int:
        dp = [[float("inf")] * n for _ in range(n)]
        res = (0, float("inf"))
        for i in range(n):
            dp[i][i] = 0
        for f, t, w in edges:
            dp[f][t] = w
            dp[t][f] = w
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j])

        for i in range(n):
            tmp = 0
            for j in range(n):
                if dp[i][j] <= distanceThreshold:
                    tmp += 1
            if tmp <= res[1]:
                res = (i, tmp)
        return res[0]
