class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        s = sum(nums)
        if s % 2 != 0: return False
        target = s // 2
        @cache      
        def rec(i, t):
            if target == t: return True
            if i == len(nums): return False
            if t > target: return False

            return rec(i+1, t+nums[i]) or rec(i+1, t)
            
        return rec(0, 0)
