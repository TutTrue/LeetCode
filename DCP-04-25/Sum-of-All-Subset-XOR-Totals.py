class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        total = 0
        n = len(nums)
        for i in range(2**n):
            cur=0
            for j in range(n):
                if i & (1 << j):
                    cur^=nums[j]
            total+=cur
        return total