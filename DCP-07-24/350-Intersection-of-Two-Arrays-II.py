class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        dic = Counter(nums1) & Counter(nums2)
        res = []
        for k, v in dic.items():
            for i in range(v):
                res.append(k)

        return res