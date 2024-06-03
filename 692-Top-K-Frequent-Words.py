class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        dic = {}
        res = []
        for word in words:
            dic[word] = dic.get(word, 0) + 1
        dic = [(-value, key) for key, value in dic.items()]
        heapify(dic)
        for i in range(k):
            res.append(heappop(dic)[1])
        return res