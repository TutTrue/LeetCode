class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        dic = defaultdict(int)
        n = len(nums)
        dis = len(set(nums))
        res = 0
        l = 0
        for r in range(n):
            dic[nums[r]] += 1
            while len(dic) == dis:
                res+= n - r
                dic[nums[l]] -= 1
                if dic[nums[l]] == 0:
                    del dic[nums[l]]
                l+=1
        return res