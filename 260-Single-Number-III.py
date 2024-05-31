class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        xor = 0
        for i in nums:
            xor^=i
        diff_bit = xor & -xor # get first diff bit from the right
        a, b = 0, 0
        for i in nums:
            if i & diff_bit:
                a^=i
            else:
                b^=i
        return [a, b]
    