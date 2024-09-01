class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        if n * m != len(original):
            return []
        res = []
        for i in range(0, len(original), n):
            res.append(original[i:i+n])
        return res