class Solution:
    def frequencySort(self, s: str) -> str:
        dic = {}
        res = [''] * len(s)
        idx = 0
        for i in s:
            dic[i] = dic.get(i, 0) + 1
        sorted_dic = sorted(dic.items(), key=lambda x: x[1], reverse=True)
        for k, v in sorted_dic:
            for i in range(v):
                res[idx] = k
                idx+=1
        return res