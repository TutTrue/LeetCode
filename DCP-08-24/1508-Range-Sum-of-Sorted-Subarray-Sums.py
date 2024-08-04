class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        subarrays = []
        n = len(nums)
        for start in range(n):
            for end in range(start, n):
                subarray = nums[start:end + 1]
                subarrays.append(sum(subarray))

        subarrays.sort()

        return sum(subarrays[left-1:right]) % (10**9 + 7)