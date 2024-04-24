class Solution:
    def tribonacci(self, n: int) -> int:
        if n < 2:
            return n
        n0, n1, n2 = 0, 1, 1
        for i in range(n-2):
            n0, n1, n2 = n1, n2, n1 + n2 + n0
        return n2