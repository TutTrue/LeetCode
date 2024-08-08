class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        result = []
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        steps = 1
        d = 0
        r, c = rStart, cStart
        result.append([r, c])

        while len(result) < rows * cols:
            for _ in range(2):
                for _ in range(steps):
                    r += directions[d][0]
                    c += directions[d][1]
                    if 0 <= r < rows and 0 <= c < cols:
                        result.append([r, c])
                d = (d + 1) % 4
            steps += 1

        return result
