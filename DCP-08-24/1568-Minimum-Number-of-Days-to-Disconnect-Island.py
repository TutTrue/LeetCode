class Solution:
    def minDays(self, grid: List[List[int]]) -> int:
        R, C = len(grid), len(grid[0])
        visited = set()
        def dfs(r, c):
            nonlocal R, C
            if r < 0 or r == R or c < 0 or c == C or grid[r][c] == 0 or (r, c) in visited:
                return

            visited.add((r, c))
            dfs(r+1, c)
            dfs(r, c+1)
            dfs(r-1, c)
            dfs(r, c-1)

        def island_count():
            count = 0
            for r in range(len(grid)):
                for c in range(len(grid[0])):
                    if grid[r][c] == 1 and (r, c) not in visited:
                        dfs(r, c)
                        count += 1
            visited.clear()
            return count

        if island_count() != 1:
            return 0
        for r in range(R):
            for c in range(C):
                if grid[r][c] == 0:
                    continue
                grid[r][c] = 0
                if island_count() != 1:
                    return 1
                grid[r][c] = 1
        return 2
