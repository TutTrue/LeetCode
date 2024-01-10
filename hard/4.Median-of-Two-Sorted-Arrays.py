# 4. Median of Two Sorted Arrays

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        r =  nums1 + nums2
        r = self.merge_sorted_arrays(nums1, nums2)
        rl = len(r)
        if rl % 2 == 1:
            return r[rl//2]
        else:
            return (r[rl//2 - 1] + r[rl//2])/2

    def merge_sorted_arrays(self, arr1: List[int], arr2: List[int]) -> List[int]:
        merged = []
        i = j = 0

        while i < len(arr1) and j < len(arr2):
            if arr1[i] < arr2[j]:
                merged.append(arr1[i])
                i += 1
            else:
                merged.append(arr2[j])
                j += 1

        merged.extend(arr1[i:])
        merged.extend(arr2[j:])

        return merged
