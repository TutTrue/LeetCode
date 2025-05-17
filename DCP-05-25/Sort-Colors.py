class Solution:
    def sortColors(self, nums: List[int]) -> None:
        \\\
        Do not return anything, modify nums in-place instead.
        \\\
        arr = [0, 0, 0]
        for i in nums:
            arr[i] += 1
        i = 0
        idx = 0
        for _ in range(3):
            while arr[i] != 0:
                nums[idx] = i
                arr[i] -= 1
                idx+=1
            i+=1
            

