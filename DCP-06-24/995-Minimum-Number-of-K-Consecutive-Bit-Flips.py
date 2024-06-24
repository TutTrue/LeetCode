class Solution:
    def minKBitFlips(self, nums: List[int], k: int) -> int:
        n, flipped, res = len(nums), 0, 0
        fp = [0] * n
        for i in range(n):
            if i >= k:
                flipped ^= fp[i - k]
            if flipped == nums[i]:
                if i + k > n:
                    return -1
                fp[i] = 1
                flipped ^= 1
                res += 1
        return res
