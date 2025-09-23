class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1, v2 = version1.split('.'), version2.split('.')
        l = len(v1) if len(v1) > len(v2) else len(v2)
        for i in range(l):
            x = y = 0
            if i < len(v1): x = int(v1[i])
            if i < len(v2): y = int(v2[i])
            if x < y: return -1
            if x > y: return 1
        return 0