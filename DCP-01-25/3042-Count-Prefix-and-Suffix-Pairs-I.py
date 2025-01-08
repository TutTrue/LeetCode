class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        def isPrefixAndSuffix(st1, st2):
            if len(st1) > len(st2): return 0
            if st1 is st2: return 1
            for i in range(len(st1)):
                if st1[i] != st2[i]: return 0
                if st1[i] != st2[len(st2) - len(st1) + i]: return 0
            return 1
        res = 0

        for i in range(len(words)):
            for j in range(i+1, len(words)):
                res += isPrefixAndSuffix(words[i], words[j])

        return res