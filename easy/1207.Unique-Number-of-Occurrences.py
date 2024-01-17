# 1207. Unique Number of Occurrences

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        dic = defaultdict(int)
        for i in arr:
            dic[i] +=1
        return len(set(dic.values())) == len(dic.values())
