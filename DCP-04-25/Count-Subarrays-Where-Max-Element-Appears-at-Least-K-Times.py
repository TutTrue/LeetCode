class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        m = max(nums)
        freq = 0
        l = 0
        res = 0
        for r in range(len(nums)):
            if nums[r] == m: freq+=1
            while freq >= k:
                if nums[l] == m: freq -= 1
                l+=1
            res += l
        return res