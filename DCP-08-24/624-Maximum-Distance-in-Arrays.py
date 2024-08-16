class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        cur_min = float('inf')
        cur_max = float('-inf')
        res = 0
        for arr in arrays:
            res = max(
                res,
                cur_max - arr[0],
                arr[-1] - cur_min
            )
            cur_min = min(cur_min, arr[0])
            cur_max = max(cur_max, arr[-1])

        return res