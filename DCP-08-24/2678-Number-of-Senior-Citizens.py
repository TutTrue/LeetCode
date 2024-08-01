class Solution:
    def countSeniors(self, details: List[str]) -> int:
        res = 0
        for p in details:
            if p[11:13] > '60':
                res+=1
        return res 