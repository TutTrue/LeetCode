class Solution:
    def resultsArray(self, queries: List[List[int]], k: int) -> List[int]:
        res = [-1] * len(queries)
        heap = []
        for i in range(len(queries)):
            temp = abs(queries[i][0]) + abs(queries[i][1])
            if len(heap) >= k:
                heappush(heap, -temp)
                heappop(heap)
            else:
                heappush(heap, -temp)
            if len(heap) == k:
                res[i] = -heap[0]
        return res