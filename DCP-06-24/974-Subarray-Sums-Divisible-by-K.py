class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        remain = defaultdict(int)
        remain[0] = 1
        prefix = 0
        res = 0
        for i in nums:
            prefix += i
            rem = prefix % k
            res += remain[rem]
            remain[rem] += 1
        return res
                