class Solution:
    def check(self, nums: List[int]) -> bool:
        down = 0
        for i in range(1, len(nums)):
            if nums[i] < nums[i-1]:
                down = i
                break
        for i in range(down+1, len(nums) + down):
            idx = i % len(nums)
            if nums[idx] < nums[idx-1]:
                return False
        return True