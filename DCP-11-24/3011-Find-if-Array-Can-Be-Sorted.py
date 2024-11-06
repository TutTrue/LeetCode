class Solution:
    def canSortArray(self, nums: List[int]) -> bool:
        bits = {}

        for i in nums:
            bits[i] = bin(i).count('1')

        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] > nums[j] and bits[nums[i]] != bits[nums[j]]:
                    return False
        return True