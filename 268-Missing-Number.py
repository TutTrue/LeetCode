class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        return reduce(lambda x, y: x - y, nums, len(nums)*(len(nums)+1) // 2)
