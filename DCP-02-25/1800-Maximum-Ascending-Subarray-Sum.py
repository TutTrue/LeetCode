class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        res = nums[0]
        cur = nums[0]
        l = 0
        for r in range(1, len(nums)):
            if nums[r] > nums[r-1]:
                cur+= nums[r]
            else:
                cur = nums[r]
            res = max(res, cur)
        return res