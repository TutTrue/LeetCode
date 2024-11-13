class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        res = 0

        nums.sort()

        for i in range(len(nums)):
            res += bisect.bisect_right(
                nums, upper - nums[i], i + 1
            ) - bisect.bisect_left(nums, lower - nums[i], i + 1)

        return res
