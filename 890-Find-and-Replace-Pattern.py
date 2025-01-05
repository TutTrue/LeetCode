class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        res = []
        def to_dict(word: str):
            dic = {}
            for i, c in enumerate(word):
                if c not in dic:
                    dic[c] = i
            return dic

        dic_pattern = to_dict(pattern)

        for word in words:
            if len(word) != len(pattern):
                continue
            dic_word = to_dict(word)
            for i in range(len(word)):
                if dic_word[word[i]] != dic_pattern[pattern[i]]:
                    break
            else:
                res.append(word)

        return res
