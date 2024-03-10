class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1 = set(nums1)
        nums2 = set(nums2)
        if len(nums1) > len(nums2):
            return [x for x in nums2 if x in nums1]
        else:
            return [x for x in nums1 if x in nums2]