class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        res = len(t)
        tp, sp = 0, 0
        while sp < len(s) and tp < len(t):
            while sp < len(s) and s[sp] != t[tp]:
                sp+=1
            if sp < len(s):
                sp+=1
                res-=1
                tp+=1

        return res