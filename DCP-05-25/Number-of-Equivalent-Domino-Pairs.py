class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        freq = defaultdict(int)
        res = 0

        for a, b in dominoes:
            key = tuple((min(a, b), max(a, b)))
            res += freq[key]
            freq[key] += 1

        return res
