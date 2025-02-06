class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        product = defaultdict(int)
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                product[nums[i] * nums[j]] += 1
        res = 0
        for i in product.values():
           pairs = (i * (i - 1)) // 2
           res += pairs * 8
        return res 