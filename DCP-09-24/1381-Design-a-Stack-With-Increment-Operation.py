class Solution:
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        freq = Counter(letters)

        def can_form_word(word):
            fw = Counter(word)
            for ch in word:
                if fw[ch] > freq[ch]:
                    return False
            return True
        
        def get_score(word):
            res = 0
            for ch in word:
                res += score[ord(ch) - ord('a')]
            return res
        
        def backtrack(i):
            if i == len(words):
                return 0
            res = backtrack(i+1)
            if can_form_word(words[i]):
                for ch in words[i]:
                    freq[ch] -= 1
                res = max(res, get_score(words[i]) + backtrack(i+1))
                for ch in words[i]:
                    freq[ch] += 1
            return res
        return backtrack(0)