class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        def is_equal(s):
            total = 0
            for i in range(len(s) // 2): total += int(s[i])
            for i in range(len(s) // 2, len(s)): total -= int(s[i])
            return True if total == 0 else False
        res = 0
        i = low if low > 9 else 10
        while i <= high:
            n = str(i)
            if len(n) & 1: i *= 10; continue
            if is_equal(n): res += 1
            i+=1

        return res