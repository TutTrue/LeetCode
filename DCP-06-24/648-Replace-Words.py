class Solution:

    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        s = set(dictionary)
        splitted = sentence.split()
        res = []
        for word in splitted:
            for i in range(len(word)):
                if word[0:i] in s:
                    res.append(word[0:i])
                    break
                if i == len(word) - 1:
                    res.append(word)
        return ' '.join(res)