class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        m = 0
        freq = defaultdict(int)
        N=len(nums)
        for i in range(1, 2**N):
            tmp = 0
            for j in range(N):
                if (i&(1<<j)):
                    tmp|=nums[j]
            freq[tmp] += 1
            m = max(m, tmp)
        return freq[m]
