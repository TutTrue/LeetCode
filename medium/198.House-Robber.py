# 198. House Robber

class Solution:
    def rob(self, nums: List[int]) -> int:
        n=len(nums)
        if n==1: return nums[0]
        p=[0]*(n+1)
        p[1]=nums[0]
        for i in range(1,n):
            p[i+1]=max(p[i-1]+nums[i], p[i])
        return p[n]
