class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        def rec(idx = 0, li = []):
            res.append(li)
            for i in range(idx, len(nums)):
                if i > idx and nums[i] == nums[i-1]:
                    continue
                rec(i+1, li+[nums[i]])
        rec()
        return res