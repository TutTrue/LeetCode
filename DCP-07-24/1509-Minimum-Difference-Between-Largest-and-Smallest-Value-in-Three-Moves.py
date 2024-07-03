class Solution:
    def minDifference(self, nums: List[int]) -> int:
        if len(nums) < 5:
            return 0
        nums.sort()
        res = float('inf')
        i, j = 0, len(nums) - 4
        while j < len(nums):
            res = min(res, nums[j] - nums[i])
            j+=1;i+=1
        return res