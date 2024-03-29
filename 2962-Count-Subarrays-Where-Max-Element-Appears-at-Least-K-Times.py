class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        freq = {}
        M = max(nums)
        res = 0
        l, r = 0, 0
        while r < len(nums):
            freq[nums[r]] = freq.get(nums[r], 0) + 1
            r += 1
            while freq.get(M, 0) >= k:
                freq[nums[l]] -= 1
                l += 1
            res += l
        return res