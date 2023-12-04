# 442. Find All Duplicates in an Array

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        s = set()
        res = []
        for i in nums:
            if i in s:
                res.append(i)
            else:
                s.add(i)
        return res
