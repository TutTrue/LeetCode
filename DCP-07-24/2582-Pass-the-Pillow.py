class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        c = 1
        direction = -1
        for i in range(time):
            if c == n or c == 1:
                direction*=-1
            c+= direction
        return c
            