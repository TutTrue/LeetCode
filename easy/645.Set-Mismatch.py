# 645. Set Mismatch

class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        dup = 1
        s = 0
        nums.sort()
        for i in range(len(nums)):
            if nums[i] == nums[i-1]:
                dup = nums[i]
            s+=nums[i]
        n = len(nums)
        return [dup, (n*(n+1) // 2) - (s - dup)]
