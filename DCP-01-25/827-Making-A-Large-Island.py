from typing import List

class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        N = len(grid)
        island_id = 2 
        island_sizes = {}

        def dfs(r, c, island_id):
            if r < 0 or r == N or c < 0 or c == N or grid[r][c] != 1:
                return 0
            
            grid[r][c] = island_id 
            size = 1
            
            size += dfs(r + 1, c, island_id)
            size += dfs(r - 1, c, island_id)
            size += dfs(r, c + 1, island_id)
            size += dfs(r, c - 1, island_id)
            
            return size

        for r in range(N):
            for c in range(N):
                if grid[r][c] == 1:
                    size = dfs(r, c, island_id)
                    island_sizes[island_id] = size
                    island_id += 1

        max_size = max(island_sizes.values(), default=0)
        
        for r in range(N):
            for c in range(N):
                if grid[r][c] == 0:
                    neighboring_islands = set()
                    for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                        nr, nc = r + dr, c + dc
                        if 0 <= nr < N and 0 <= nc < N and grid[nr][nc] > 1:
                            neighboring_islands.add(grid[nr][nc])
                    
                    potential_size = 1
                    for island in neighboring_islands:
                        potential_size += island_sizes[island]
                    
                    max_size = max(max_size, potential_size)

        return max_size
