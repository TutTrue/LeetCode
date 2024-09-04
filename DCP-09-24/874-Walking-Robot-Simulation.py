class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        x, y = 0, 0
        direction = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        d = 0
        res = 0

        obstacles = { tuple(o) for o in obstacles }

        for c in commands:
            if c == -1:
                d = (d + 1) % 4
            elif c == -2:
                d = (d - 1) % 4
            else:
                dx, dy = direction[d]
                for _ in range(c):
                    if (dx+x, dy+y) in obstacles:
                        break
                    x, y = dx + x, dy + y
                res = max(res, x**2 + y**2)
        return res
