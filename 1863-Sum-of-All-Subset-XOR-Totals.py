class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        total = 0
        def rec(i=0, cur=0):
            nonlocal total
            if i == len(nums):
                total+=cur
                return
            rec(i+1, cur)
            rec(i+1, cur^nums[i])
        rec()
        return total