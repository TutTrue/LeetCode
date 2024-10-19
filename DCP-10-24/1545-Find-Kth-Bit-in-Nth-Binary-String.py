class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        def reverse_invert(s):
            li = ['1']
            for c in reversed(s):
                if c == '1':
                    li.append('0')
                else:
                    li.append('1')
            return li
        s = ['0']
        for i in range(n):
            s += reverse_invert(s)
        return s[k-1]