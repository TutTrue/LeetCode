class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        res = 0
        cur_max = 0
        for i, n in enumerate(arr):
            cur_max = max(cur_max, n)
            if cur_max == i:
                res+=1
        return res