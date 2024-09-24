class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        s = set()
        res = 0
        for i in arr1:
            while i:
                s.add(i)
                i //= 10
        
        for i in arr2:
            while i:
                if i in s:
                    res = max(res, len(str(i)))
                    break
                i //= 10
        return res