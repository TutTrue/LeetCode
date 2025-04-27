class Solution:
    def countSubarrays(self, nums: List[int]) -> int:
        i, j, k = 0, 1, 2
        res = 0
        while k < len(nums):
            if (nums[i] + nums[k]) * 2 == nums[j]:
                res += 1
            i+=1
            j+=1
            k+=1
        return res