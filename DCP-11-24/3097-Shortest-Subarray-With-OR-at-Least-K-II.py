class Solution:
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        res = float('inf')
        l = 0
        total = 0
        bits = [0] * 32
        for r in range(len(nums)):
            for i in range(32):
                if nums[r] & (1 << i):
                    bits[i] += 1

            cur =0 
            for i in range(32):
                if bits[i]:
                    cur += (1 << i)

            while l <= r and cur >= k:
                res = min(res, r - l + 1)
                for i in range(32):
                    if nums[l] & (1 << i):
                        bits[i] -= 1
                cur = 0
                for i in range(32):
                    if bits[i]:
                        cur += (1 << i)
                l+=1

        return -1 if res == float('inf') else res