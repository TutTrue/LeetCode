class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], workers: List[int]) -> int:
        difficulty_profit = [(profit[i], difficulty[i]) for i in range(len(difficulty))]
        difficulty_profit.sort()
        profit, difficulty = zip(*difficulty_profit)
        def get_max_profit(worker):
            j = len(profit) - 1
            while j >=0:
                if difficulty[j] <= worker:
                    return profit[j]
                j-=1
            return 0
        total = 0
        for worker in workers:
            total += get_max_profit(worker)
        return total
            
            