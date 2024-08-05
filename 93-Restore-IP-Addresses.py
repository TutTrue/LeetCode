class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        res = []

        def rec(i=0, dots=0, ip=\\):
            if dots == 4 and i == len(s):
                res.append(ip[:-1])
                return
                
            if dots >= 4:
                return
                
            for j in range(1, 4):
                if i + j <= len(s) and int(s[i : i + j]) <= 255:
                    if j > 1 and s[i] == \0\:
                        continue
                    rec(i + j, dots + 1, ip + s[i : i + j] + \.\)

        rec()
        return res
