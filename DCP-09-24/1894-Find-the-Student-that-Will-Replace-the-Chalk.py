class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = [''] * (len(word1) + len(word2))
        idx = 0
        i = 0
        while i < len(word1) and i < len(word2):
            res[idx] = word1[i]
            idx+=1
            res[idx] = word2[i]
            idx+=1
            i+=1
        if i < len(word1):
            res[idx+1:] = word1[i:]
        if i < len(word2):
            res[idx+1:] = word2[i:]
        return ''.join(res)