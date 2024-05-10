class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        res = []
        for i in range(len(arr)):
            for j in range(i+1, len(arr)):
                heapq.heappush(res, (-arr[i]/arr[j], [arr[i], arr[j]]))
                if len(res) > k:
                    heapq.heappop(res)
        return heapq.heappop(res)[1]