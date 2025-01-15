class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        diff = num1.bit_count() - num2.bit_count()
        if diff > 0:
            for _ in range(diff): num1 &= num1 - 1
        else:
            for _ in range(-diff): num1 |= num1 + 1
        return num1