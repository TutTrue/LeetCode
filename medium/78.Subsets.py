# 78. Subsets

class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        def rec(idx = 0, li = []):
            res.append(li)
            for i in range(idx, len(nums)):
                if i > idx and nums[i] == nums[i-1]:
                    continue
                rec(i+1, li+[nums[i]])
            return res
        return rec()
