class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], k: int) -> float:
        m = float('inf')
        ratio = []
        for i in range(len(quality)):
            ratio.append((wage[i] / quality[i], quality[i])) # (ratio, quality)
        ratio.sort(key=lambda x: x[0])
        max_heap = []
        total = 0
        for rate, q in ratio:
            heappush(max_heap, -q)
            total += q
            if len(max_heap) > k:
                total -= -heappop(max_heap)
            if len(max_heap) == k:
                m = min(m, total* rate)
        return m