class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        vowel = "aeiou"
        res = [0] * len(queries)
        words[0] = 1 if (words[0][0] in vowel and words[0][-1] in vowel) else 0
        for i in range(1, len(words)):
            if words[i][0] in vowel and words[i][-1] in vowel:
                words[i] = words[i - 1] + 1
            else:
                words[i] = words[i - 1]

        for i in range(len(queries)):
            l, r = queries[i]
            res[i] = words[r] - (words[l - 1] if l > 0 else 0)

        return res
