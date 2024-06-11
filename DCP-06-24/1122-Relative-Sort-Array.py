class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        freq = {}
        for i in arr1:
            freq[i] = freq.get(i, 0) + 1

        idx = 0
        for i in arr2:
            n = freq[i]
            while n > 0:
                arr1[idx] = i
                idx+=1
                n-=1
            del freq[i]
        for k, v in sorted(freq.items()):
            n = v
            while n > 0:
                arr1[idx] = k
                n-=1
                idx+=1
        return arr1