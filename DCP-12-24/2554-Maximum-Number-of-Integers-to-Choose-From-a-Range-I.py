class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        s = set(banned)
        res = 0
        count = 0
        for i in range(1, n+1):
            if i not in s and count + i <= maxSum:
                res+=1
                count+=i
        return res
