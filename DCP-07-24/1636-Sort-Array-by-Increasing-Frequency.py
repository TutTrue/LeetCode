class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        x = {}
        res = []
        for i in nums:
            x[i] = x.get(i, 0) + 1

        for v ,f in sorted(x.items(), key=lambda i: (i[1], -i[0])):
            res.extend([v] * f)
        return res