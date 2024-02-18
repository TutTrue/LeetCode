class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        dic = defaultdict(int)
        for i in arr:
            dic[i]+=1
        for ky, v in sorted(dic.items(), key=lambda item: item[1]):
            for i in range(v):
                if k > 0:
                    dic[ky]-=1
                    k-=1
                else:
                    break
        return reduce(lambda acc, value: acc + 1 if value != 0 else acc, dic.values(), 0)