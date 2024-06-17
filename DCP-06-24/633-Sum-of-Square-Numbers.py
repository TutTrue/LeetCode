class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        if c == 0:
            return True
        for a in range(int(sqrt(c) + 1)):
            b_sq = c - a*a
            if b_sq >= 0:
                b = int(math.sqrt(b_sq))
                if b * b == b_sq:
                    return True
        return False