class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        res = 0
        prefix = nums[0]
        diff = 0
        for k in range(1, len(nums)):
            res = max(res, diff * nums[k])
            prefix = max(prefix, nums[k])
            diff = max(diff, prefix - nums[k])

        return res