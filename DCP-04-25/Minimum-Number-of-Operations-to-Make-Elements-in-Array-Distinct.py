class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        s = set()
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] in s:
                return ((i + 1) + ((3 - (i + 1)) % 3)) // 3
            s.add(nums[i])
        return 0