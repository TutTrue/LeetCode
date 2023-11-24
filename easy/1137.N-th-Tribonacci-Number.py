# 1137. N-th Tribonacci Number
class Solution(object):
    def tribonacci(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 0
        f1, f2,f3 = 0, 1, 1
        for i in range(n - 2):
            f1, f2, f3 = f2, f3, f1+f2+f3
        return f3




    # def tribonacci(self, n, mem={}):

        # if n in mem:
        #     return mem[n]
        # if n == 0:
        #     return 0
        # if n < 3:
        #     return 1
        # mem[n] = self.tribonacci(n - 1, mem) + self.tribonacci(n - 2, mem) + self.tribonacci(n - 3, mem)
        # return mem[n]

