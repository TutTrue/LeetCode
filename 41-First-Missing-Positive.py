class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums = list(set(nums))
        nums.sort()
        x = 0
        i = 0
        while i < len(nums) and nums[i] < 0:
            i+=1
        if i < len(nums) - 1 and nums[i] == 0:
            i+=1
        for idx, j in enumerate(nums[i:]):
            if idx + 1 != j:
                x = idx + 1
                return x
            x = idx + 1

        return x + 1