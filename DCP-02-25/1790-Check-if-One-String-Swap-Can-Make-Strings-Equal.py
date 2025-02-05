class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        if len(s1) != len(s2): return False
        diff1 = -1
        diff2 = -1
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                if diff1 != -1 and diff2 != -1: return False
                if diff1 == -1:
                    diff1 = i
                else:
                    diff2 = i
        return s1[diff1] == s2[diff2] and s1[diff2] == s2[diff1]
            