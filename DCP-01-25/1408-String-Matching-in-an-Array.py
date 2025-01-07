class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        res = []
        for sub in words:
            for word in words:
                if sub is word: continue
                if len(sub) > len(word): continue
                if sub in word: res.append(sub); break

        return res
