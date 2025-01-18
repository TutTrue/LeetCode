class Solution:
    dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    def minCost(self, grid: List[List[int]]) -> int:
        num_rows, num_cols = len(grid), len(grid[0])

        pq = [(0, 0, 0)]
        min_cost = [[float("inf")] * num_cols for _ in range(num_rows)]
        min_cost[0][0] = 0

        while pq:
            cost, row, col = heapq.heappop(pq)

            if min_cost[row][col] != cost:
                continue

            for d, (dx, dy) in enumerate(self.dirs):
                new_row, new_col = row + dx, col + dy

                if 0 <= new_row < num_rows and 0 <= new_col < num_cols:
                    new_cost = cost + (d != (grid[row][col] - 1))

                    if min_cost[new_row][new_col] > new_cost:
                        min_cost[new_row][new_col] = new_cost
                        heapq.heappush(pq, (new_cost, new_row, new_col))

        return min_cost[num_rows - 1][num_cols - 1]