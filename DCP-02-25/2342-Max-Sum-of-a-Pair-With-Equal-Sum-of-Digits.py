class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        def digitSum(x):
            s=0
            while x>0:
                q, r=divmod(x, 10)
                s+=r
                x=q
            return s

        maxD=[0]*82
        res=-1
        for x in nums:
            D=digitSum(x)
            if maxD[D]>0:
                res=max(res, maxD[D]+x)
            maxD[D]=max(maxD[D], x)
        return res