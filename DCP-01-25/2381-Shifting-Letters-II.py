class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        ops = [0] * (len(s) + 1)
        for l, r, d in shifts:
            ops[r + 1] += 1 if d else -1
            ops[l] += -1 if d else 1

        res = [ord(c) - ord("a") for c in s]
        cur_shift = 0
        for i in range(len(ops) - 1, -1, -1):
            cur_shift += ops[i]
            res[i - 1] = (cur_shift + res[i - 1]) % 26

        return "".join([chr(ord("a") + i) for i in res])
