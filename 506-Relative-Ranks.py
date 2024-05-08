class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        dic = {}
        for i, v in enumerate(sorted(score, reverse=True)):
            if i == 0:
                dic[v] = \Gold Medal\
            elif i == 1:
                dic[v] = \Silver Medal\
            elif i == 2:
                dic[v] = \Bronze Medal\
            else:
                dic[v] = str(i+1)
        
        return [dic[v] for v in score]