class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        res = 0
        for i in range(len(nums)):
            nums[i] *= -1
        heapify(nums)
        for i in range(k):
            tmp = -heappop(nums)
            res += tmp
            heappush(nums, -math.ceil(tmp / 3))
        return res