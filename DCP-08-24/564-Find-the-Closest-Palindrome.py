class Solution:
    def nearestPalindromic(self, n: str) -> str:
        def helper(n, additive):
            l = len(n)
            if l == 0:
                return 0
            first_half = str(int(n[:l // 2 + l % 2]) + additive)
            return int(first_half + first_half[(-1 - l%2)::-1])
        res = None
        pals = [
            helper(n, 0),
            helper(n, 1),
            helper(n, -1),
            helper(\9\*(len(n) - 1), 0),
            helper(\1\ + \0\ * (len(n)), 0)
        ]
        print(pals)
        for i in pals:
            if str(i) == n:
                pass
            else:
                if res is None or abs(res - int(n)) > abs(i - int(n)) or (abs(res - int(n)) == abs(i - int(n)) and i < int(n)):
                    res = i
        return str(res)
