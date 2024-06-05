class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        dic = Counter(words[0])
        for word in words:
            dic &= Counter(word)
        return list(dic.elements())