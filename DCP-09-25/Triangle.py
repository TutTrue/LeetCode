class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        @lru_cache(None)
        def dfs(i: int, j: int) -> int:
            if i == len(triangle) - 1:
                return triangle[i][j]
            return triangle[i][j] + min(dfs(i+1, j), dfs(i+1, j+1))

        return dfs(0, 0)
