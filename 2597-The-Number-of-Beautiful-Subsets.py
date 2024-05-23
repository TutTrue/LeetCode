class Solution:
    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        nums.sort()
        res = -1
        def is_beautiful(arr):
            if arr[-1] - k in arr:
                return False
            return True 
        def rec(i=0, cur=[]):
            nonlocal res
            if cur and not is_beautiful(cur):
                return
            if i == len(nums):
                res+=1
                return
            rec(i+1, cur)
            rec(i+1, cur+[nums[i]])
        rec()
        return res