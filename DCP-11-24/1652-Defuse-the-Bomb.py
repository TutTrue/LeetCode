class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        res = [0] * len(code)
        if k == 0: return res
        d = 1 if k > 0 else -1
        for r in range(len(code)):
            s = 0
            for i in range(r + d, r + k + d, d):
                s += code[i % len(code)]
            res[r] = s
        return res