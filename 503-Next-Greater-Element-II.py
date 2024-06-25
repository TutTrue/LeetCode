class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        res = [-1] * len(nums)
        for i in range(len(nums)):
            for j in range(i, len(nums)+i):
                if nums[j % len(nums)] > nums[i]:
                    res[i] = nums[j % len(nums)]
                    break
        return res
