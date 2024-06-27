class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        dic = defaultdict(int)
        for n1, n2 in edges:
            dic[n1] += 1
            dic[n2] += 1
        for e, f in dic.items():
            if f == len(edges):
                return e
                
        return -1