class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        freq = defaultdict(int)
        for i in nums:
            freq[i] += 1
        m = max(freq.values())
        count =0
        for v in freq.values():
            if v == m:
                count+=m
        return count