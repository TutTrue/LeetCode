class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        c1 = defaultdict(int)
        c2 = defaultdict(int)
        res = []
        acc = 0
        for a, b in zip(A, B):
            c1[a] += 1
            c2[b] += 1
            if c1[b] == c2[b]: acc += 1
            if c2[a] == c1[a]: acc += 1
            if a == b: acc -= 1
            res.append(acc)
        return res
