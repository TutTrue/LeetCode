class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        m = 0
        dic = defaultdict(int)
        res = 0
        for i in nums:
            dic[i] += 1
            m = max(m, dic[i])
        for v in dic.values():
            if v == m:
                res += v

        return res
