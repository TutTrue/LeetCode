class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        square = list(map(lambda x: x * x, nums))
        square.sort()
        return square