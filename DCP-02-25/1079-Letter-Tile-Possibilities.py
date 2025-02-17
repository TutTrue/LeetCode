class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        v = set()
        res = 0
        freq = {}
        for t in tiles:
            if t not in freq:
                freq[t] = 0
            freq[t] += 1

        def backtrack(s):
            nonlocal res
            if len(s) == len(tiles):
                return
            for k, val in freq.items():
                if val == 0:
                    continue
                s += k
                freq[k] -= 1
                if s not in v:
                    res += 1
                    v.add(s)
                backtrack(s)
                freq[k] += 1
                s = s[:-1]

        backtrack("")
        return res
