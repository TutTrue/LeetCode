class Solution:
    def longestPalindrome(self, s: str) -> str:
        def isPali(start, end):
            while start >= 0 and end < len(s) and s[start] == s[end]:
                start-=1
                end+=1
            return (start+1, end)
        res = ''
        for i in range(len(s)):
            start, end = isPali(i,i)
            if end - start + 1 > len(res):
                res = s[start:end]
            start, end = isPali(i,i+1)
            if end - start + 1 > len(res):
                res = s[start:end]
            
        return res