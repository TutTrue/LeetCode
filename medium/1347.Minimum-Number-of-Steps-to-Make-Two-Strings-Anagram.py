# 1347. Minimum Number of Steps to Make Two Strings Anagram

class Solution:
    def minSteps(self, s: str, t: str) -> int:
        freqs = [0] * 26
        freqt = [0] * 26
        steps = 0

        for i in range(len(s)):
            freqs[ord(s[i]) - 97] +=1
            freqt[ord(t[i]) - 97] +=1

        for i in range(len(freqs)):
            steps += abs(freqs[i] - freqt[i])

        return steps // 2
