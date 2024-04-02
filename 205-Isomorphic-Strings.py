class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        ds = {}
        dt = {}
        for i in range(len(s)):
            if s[i] in ds and t[i] in dt:
                if ds[s[i]] != dt[t[i]]:
                    return False
            else:
                if (s[i] in ds and t[i] not in dt) or (s[i] not in ds and t[i] in dt):
                    return False
                ds[s[i]] = i
                dt[t[i]] = i
        return True

    def isIsomorphic2(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        dis = []
        dit = []
        for i in range(len(s)):
            if s.index(s[i]) != t.index(t[i]):
                return False
        return True
