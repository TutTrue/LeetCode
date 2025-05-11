class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        c = 0
        for i in arr:
            if i & 1:
                if c == 2: return True
                else: c+=1
            else:
                c=0
        return False