class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        cache = {}

        def dfs(l):
            if l > high:
                return 0

            if l in cache:
                return cache[l]

            cache[l] = 1 if l >= low else 0
            cache[l] += dfs(l + one) + dfs(l + zero)
            return cache[l] % (10**9 + 7)

        return dfs(0)
