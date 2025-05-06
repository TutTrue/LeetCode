class Solution:
    def numTilings(self, n: int) -> int:
        if n == 1 or n == 2:
            return n
        if n == 3: return 5
        l1 = 1
        l2 = 2
        l3 = 5
        for i in range(n - 3):
            t = l3 * 2 + l1
            l1 = l2
            l2 = l3
            l3 = t
        return l3 % (10**9 + 7)