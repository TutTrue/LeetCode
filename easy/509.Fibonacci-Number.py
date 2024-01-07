# 509. Fibonacci Number

class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0 or n == 1:
            return n
        one, two = 0, 1
        for i in range(n - 1):
            one, two = two, one + two
        return two
