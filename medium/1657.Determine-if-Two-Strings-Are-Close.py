# 1657. Determine if Two Strings Are Close

class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False
        freq1 = [0] * 26
        freq2 = [0] * 26
        for i in range(len(word1)):
            freq1[ord(word1[i]) - 97] += 1
            freq2[ord(word2[i]) - 97] += 1
        for i in range(26):
            if i > 0:
                if freq1[i] == 0 and freq2[i] != 0:
                    return False

        return sorted(freq1) == sorted(freq2)        
