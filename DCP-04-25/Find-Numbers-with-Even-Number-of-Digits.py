class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        res = 0
        for i in nums:
            d = 0
            while i > 0:
                i//=10
                d+=1
            if not d & 1: res+=1
        return res