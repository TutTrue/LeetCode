class Solution:
    def minimumMountainRemovals(self, nums: List[int]) -> int:
        N = len(nums)

        lis = [1] * N
        lds = [1] * N

        for i in range(N):
            for j in range(i):
                if nums[i] > nums[j]:
                    lis[i] = max(lis[i], 1 + lis[j])

        for i in reversed(range(N)):
            for j in range(i+1, N):
                if nums[i] > nums[j]:
                    lds[i] = max(lds[i], 1 + lds[j])
        
        res = N
        for i in range(N):
            if lis[i] > 1 and lds[i] > 1:
                res = min(
                    res,
                    N - lis[i] - lds[i] + 1
                )

        return res

        