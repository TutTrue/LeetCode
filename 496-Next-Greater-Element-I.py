class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        dic = {}
        res = [-1] * len(nums1)
        for i in range(len(nums2)):
            dic[nums2[i]] = i
        for i in range(len(nums1)):
            for j in range(dic[nums1[i]]+1, len(nums2)):
                if nums2[j] > nums1[i]:
                    res[i] = nums2[j]
                    break
        return res