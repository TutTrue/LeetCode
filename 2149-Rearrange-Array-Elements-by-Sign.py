class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        pos = [x for x in nums if x > 0]
        neg = [x for x in nums if x < 0]
        res = []
        for p, n in zip(pos, neg):
            res.append(p)
            res.append(n)
        return res