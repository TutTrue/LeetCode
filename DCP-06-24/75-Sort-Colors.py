class Solution:
    def sortColors(self, nums: List[int]) -> None:
        \\\
        Do not return anything, modify nums in-place instead.
        \\\
        freq = [0, 0, 0]
        for i in nums:
            freq[i] += 1
        idx = 0
        for i, v in enumerate(freq):
            while v:
                nums[idx] = i
                v-=1
                idx+=1