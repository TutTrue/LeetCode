class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        max_freq = Counter()
        for word in words2:
            max_freq |= Counter(word)

        res = []
        for word in words1:
            freq = Counter(word)
            if all(freq[char] >= max_freq[char] for char in max_freq):
                res.append(word)

        return res
