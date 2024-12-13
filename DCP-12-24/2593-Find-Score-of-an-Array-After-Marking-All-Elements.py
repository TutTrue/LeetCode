class Solution:
    def findScore(self, nums: List[int]) -> int:
        heap = [(v, i) for i, v in enumerate(nums)]
        marked = set()
        heapify(heap)
        score = 0

        while heap:
            val, idx = heappop(heap)
            if idx not in marked:
                score += val
                marked.add(idx)
                marked.add(idx - 1)
                marked.add(idx + 1)
        return score
