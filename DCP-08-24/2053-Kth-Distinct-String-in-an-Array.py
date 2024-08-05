class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        freq = Counter(arr)
        for s in arr:
            if freq[s] != 1:
                continue
            if k == 1:
                return s
            k-=1 
        return ''