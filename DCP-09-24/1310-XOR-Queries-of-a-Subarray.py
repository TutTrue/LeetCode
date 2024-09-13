class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        res = [0] * len(queries)
        for i in range(1, len(arr)):
            arr[i] ^= arr[i-1]

        for i in range(len(queries)):
            l, r = queries[i]
            res[i] = arr[r] ^ (arr[l-1] if l > 0 else 0)
            
        return res