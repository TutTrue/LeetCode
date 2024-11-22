class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        freq = defaultdict(int)
        res = 0
        for row in matrix:
            r = tuple(row)

            if row[0]:
                r = tuple(0 if n else 1 for n in row)

            freq[r] += 1
            res = max(res, freq[r])

        return res