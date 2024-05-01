class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        word = list(word)
        for i in range(len(word)):
            if word[i] == ch:
                l, r = 0, i
                while r > l:
                    word[l], word[r] = word[r], word[l]
                    l+=1
                    r-=1
                break
        return ''.join(word)