class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        neg = 0
        min_neg = abs(matrix[0][0])
        s = 0
        for i in matrix:
            for n in i:
                s+=abs(n)
                min_neg = min(min_neg, abs(n))
                if n <= 0:
                    neg+=1
        return s if neg % 2 == 0 else s - (min_neg * 2)