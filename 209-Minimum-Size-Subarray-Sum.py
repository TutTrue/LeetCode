class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        m = float('inf')
        l, total = 0, 0
        for r in range(len(nums)):
            total+=nums[r]
            while target <= total:
                m = min(m, r - l + 1)
                total-=nums[l]
                l+=1
        return 0 if m == float('inf') else m