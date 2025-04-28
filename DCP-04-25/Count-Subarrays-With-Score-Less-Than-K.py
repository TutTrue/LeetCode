class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        l = 0
        s = 0
        n = 0
        res = 0
        for r in range(len(nums)):
            s+= nums[r]
            n+=1
            while s * n >= k:
                s -= nums[l]
                l += 1
                n-=1
            res+= r - l + 1
        return res