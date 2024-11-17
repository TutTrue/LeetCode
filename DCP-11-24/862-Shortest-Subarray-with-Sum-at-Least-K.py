class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        res = float('inf')
        heap = []
        s = 0
        for r in range(len(nums)):
            s += nums[r]

            if s >= k:
                res = min(res, r + 1)

            while heap and s - heap[0][0] >= k:
                _, idx = heappop(heap)
                res = min(res, r - idx)

            heappush(heap, (s, r))
        return -1 if res == float('inf') else res
