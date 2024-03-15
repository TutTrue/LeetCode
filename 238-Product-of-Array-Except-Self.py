class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zeros = 0
        total = 1
        res = [0] * len(nums)

        for i in nums:
            if i == 0:
                zeros+=1
                continue
            total *= i

        if zeros > 1:
            return [0] * len(nums)

        if zeros == 1:
            index = nums.index(0)
            total = 1
            for i in range(len(nums)):
                if i != index:
                    total *= nums[i]
            return [0] * index + [total] + [0] * (len(nums) - index - 1)

        for i in range(len(nums)):
            res[i] = total//nums[i]

        return res