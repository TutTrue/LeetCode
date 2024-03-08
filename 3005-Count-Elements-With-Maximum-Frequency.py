class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        freq = defaultdict(int)
        for i in nums:
            freq[i] += 1
        sorted_freq = sorted(freq.values(), reverse=True)
        i = 0
        count = 0
        while i < len(sorted_freq) and sorted_freq[0] == sorted_freq[i]:
            count += sorted_freq[i]
            i+=1
        return count