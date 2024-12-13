class Solution:
    def findScore(self, nums: List[int]) -> int:
        heap = [(v, i) for i, v in enumerate(nums)]
        heapify(heap)
        score = 0

        while heap:
            val, idx = heappop(heap)
            if nums[idx]:
                score += val
                # mark with zero
                nums[idx] = 0
                if idx > 0:
                    nums[idx - 1] = 0
                if idx < len(nums) - 1:
                    nums[idx + 1] = 0
        return score