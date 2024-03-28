class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        l, r = 0, 0
        res = 0
        dic = {}
        while r < len(nums):
            dic[nums[r]] = dic.get(nums[r], 0) + 1
            while dic[nums[r]] > k:
                dic[nums[l]] -= 1
                l+=1
            res = max(res, r - l + 1)
            r += 1
        return res