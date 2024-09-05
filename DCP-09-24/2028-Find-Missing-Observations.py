class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        res = []
        missing_sum = mean * (len(rolls) + n) - sum(rolls)
        if missing_sum / n > 6 or missing_sum < n:
            return []

        while n != 0:
            el = min(6, missing_sum - n + 1)
            res.append(el)
            missing_sum -= el
            n-=1
        return res