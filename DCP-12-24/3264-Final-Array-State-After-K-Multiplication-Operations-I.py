class Solution:
    def getFinalState(self, nums: List[int], k: int, x: int) -> List[int]:
        heap = [(v, i) for i, v in enumerate(nums)]
        heapify(heap)
        for i in range(k):
            v, idx = heappop(heap)
            nums[idx] = v * x
            heappush(heap, (v*x, idx))
        return nums
