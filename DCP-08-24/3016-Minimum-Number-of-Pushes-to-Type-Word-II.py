class Solution:
    def minimumPushes(self, word: str) -> int:
        freq = Counter(word)
        res = 0
        weight = 0
        freq = sorted(freq.items(), key=lambda x: x[1], reverse=True)
        for i, (_, n) in enumerate(freq):
            if i % 8 == 0:
                weight+=1
            res += weight * n
        return res