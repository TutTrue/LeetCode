class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        res = [0] * (len(nums) - k + 1)
        for i in range(len(nums) - k + 1):
            m = nums[i]
            for j in range(i + 1, i + k):
                if nums[j] != nums[j-1] + 1:
                    m = -1
                    break
                m = nums[j]
            res[i] = m
        return res
