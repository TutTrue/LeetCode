class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        freq = defaultdict(int)
        l = 0
        s = 0
        res = 0
        for r in range(len(nums)):
            freq[nums[r]] += 1
            s+=nums[r]
            if r - l + 1 > k:
                s-=nums[l]
                freq[nums[l]] -= 1
                if not freq[nums[l]]:
                    del freq[nums[l]]
                l+=1
            if r - l + 1 == k and len(freq.keys()) == k:
                res = max(res, s)

        return res
