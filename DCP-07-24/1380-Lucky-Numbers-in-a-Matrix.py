class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        row_min = set([min(row) for row in matrix])
        col_max = set([max(row) for row in zip(*matrix)])
        return row_min & col_max