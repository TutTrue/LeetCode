#1679. Max Number of K-Sum Pairs

class Solution(object):
    def maxOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort()
        count = 0
        l = 0
        r = len(nums) - 1
        while r > l:
            if nums[l] + nums[r] == k:
                count+=1
                l +=1
                r -=1
            elif nums[l] + nums[r] > k:
                r -=1
            else:
                l +=1
        return count
