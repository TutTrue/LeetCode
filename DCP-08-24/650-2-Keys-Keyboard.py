class Solution:
    def minSteps(self, n: int) -> int:
        res = 0
        divisor = 2
        while n > 1:
            while n % divisor == 0:
                res+=divisor
                n //= divisor
            divisor += 1
        return res
