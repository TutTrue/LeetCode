class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1 = version1.split('.')
        v2 = version2.split('.')
        if len(v1) > len(v2):
            v2.extend(['0'] * (len(v1) - len(v2)))
        elif len(v2) > len(v1):
            v1.extend(['0'] * (len(v2) - len(v1)))
        for x1, x2 in zip(v1, v2):
            if int(x1) > int(x2):
                return 1
            if int(x1) < int(x2):
                return -1
        return 0