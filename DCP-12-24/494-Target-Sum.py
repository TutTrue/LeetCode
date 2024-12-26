class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        @cache
        def rec(i, s):
            if i == len(nums):
                return 1 if target == s else 0
            return rec(i + 1, s + nums[i]) + rec(i + 1, s - nums[i])

        return rec(0, 0)
