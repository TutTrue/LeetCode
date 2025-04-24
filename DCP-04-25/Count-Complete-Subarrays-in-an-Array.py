class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        n = len(nums)
        dis = len(set(nums))
        res = 0
        for i in range(n):
            s =set()
            for j in range(i, n):
                s.add(nums[j])
                if len(s) == dis: res +=1
        return res