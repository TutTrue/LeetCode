class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        xor = 0

        for i in nums:
            xor ^= i

        mask = (1 << maximumBit) - 1 # (2 ** maximumBit) - 1
        res = []
        for i in reversed(nums):
            res.append(xor ^ mask)
            xor ^= i
        return res