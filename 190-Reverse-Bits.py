class Solution:
    def reverseBits(self, n: int) -> int:

        x = list(bin(n))
        x.pop(0)
        x.pop(0)
        res = ['0'] * 32
        j = 0
        for i in range(len(x)-1, -1, -1):
            res[j] = x[i]
            j+=1
        return int(''.join(res), 2)