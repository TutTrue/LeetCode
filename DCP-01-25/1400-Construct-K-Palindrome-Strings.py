class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        if len(s) < k: return False
        if len(s) == k: return True
        freq = Counter(s)
        odd = 0
        for v in freq.values():
            if v % 2 == 1: odd += 1
        return odd <= k