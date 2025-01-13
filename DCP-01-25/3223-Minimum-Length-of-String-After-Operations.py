class Solution:
    def minimumLength(self, s: str) -> int:
        freq = Counter(s)
        res = 0
        for k, v in freq.items():
            res += 1 if v % 2 else 2

        return res