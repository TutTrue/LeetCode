class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        nums.sort()
        count = 0
        for i in range(1, len(nums)):
            if nums[i] <= nums[i-1]:
                increase = abs(nums[i] - nums[i-1]) + 1
                count+= increase
                nums[i]+= increase
        return count