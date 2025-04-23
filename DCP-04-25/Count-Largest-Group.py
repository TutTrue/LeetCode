class Solution:
    def countLargestGroup(self, n: int) -> int:
        dic = defaultdict(int)
        m = 0
        for i in range(1, n+1):
            acc = 0
            while i > 0:
                acc += i % 10
                i //= 10
            dic[acc] += 1
            m = max(m, dic[acc])
        res = 0
        for v in dic.values():
            if v == m: res += 1

        return res