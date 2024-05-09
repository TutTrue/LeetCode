class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        happiness.sort(reverse=True)
        s = 0
        for i in range(k):
            if happiness[i] - i < 0:
                return s
            s+=happiness[i] - i
        return s