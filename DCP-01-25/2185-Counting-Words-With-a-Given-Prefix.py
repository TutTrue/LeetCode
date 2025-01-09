class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        res = 0
        for word in words:
            if len(pref) > len(word): continue
            for i in range(len(pref)):
                if pref[i] != word[i]: break
            else:
                res+=1

        return res