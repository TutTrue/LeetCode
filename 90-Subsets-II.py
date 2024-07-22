class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        nums.sort()
        N=len(nums)
        for i in range(1, 2**N):
            li =[]
            for j in range(N):
                if (i&(1<<j)):
                    li.append(nums[j])
            if li not in res:
                res.append(li)
        return res