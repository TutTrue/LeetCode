class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        total = 0
        good = 0
        dic = defaultdict(int)
        for i in range(len(nums)):
            total += i
            good += dic[nums[i] - i]
            dic[nums[i] - i] += 1
        return total - good