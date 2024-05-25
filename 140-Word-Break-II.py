class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        cur = []
        res = []
        wordDict = set(wordDict)
        def backtrack(i):
            if i == len(s):
                print(1)
                res.append(' '.join(cur))
                return
            
            for j in range(i, len(s)):
                word = s[i:j+1]
                if word in wordDict:
                    cur.append(word)
                    backtrack(j+1)
                    cur.pop()
        backtrack(0)
        return res