class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        nums.sort()
        dic = {}
        res = -1
        for i in reversed(nums):
            if i * i in dic:
                dic[i] = dic[i*i] + 1
                res = max(res, dic[i])
            else:
                dic[i] = 1
        return res