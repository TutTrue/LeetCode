class Solution:
    def specialArray(self, nums: List[int]) -> int:
        def bisetree(arr, target):
            s, e = 0, len(arr)
            while s < e:
                mid = (s + e) // 2
                if arr[mid] >= target:
                    e = mid
                else:
                    s = mid + 1
            return s
        nums.sort()
        for i in range(len(nums) + 1):
            if len(nums) - bisetree(nums, i) == i:
                return i
        return -1
            