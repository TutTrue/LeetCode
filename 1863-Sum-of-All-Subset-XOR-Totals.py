class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        total = 0
        def rec(i=0, arr=[]):
            nonlocal total
            if i == len(nums):
                total += reduce(xor, arr, 0)
                return
            rec(i+1, arr)
            rec(i+1, arr+[nums[i]])
        rec()
        return total