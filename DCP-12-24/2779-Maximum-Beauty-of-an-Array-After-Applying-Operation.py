class Solution:
    def maximumBeauty(self, nums: List[int], k: int) -> int:
        nums.sort()
        res = 0
        l = r = 0
        while r < len(nums):
            if nums[l] + k >= nums[r] - k:
                res = max(res, r - l + 1)
                r+=1
                continue
            l += 1
        
        return res