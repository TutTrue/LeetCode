class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        dic = {}
        sorted_arr = sorted(set(arr))
        for i, v in enumerate(sorted_arr):
            if v not in dic:
                dic[v] = i + 1
        for i in range(len(arr)):
            arr[i] = dic[arr[i]]
        return arr
