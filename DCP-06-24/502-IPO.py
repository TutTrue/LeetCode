class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        capital_profit = [(capital[i], profits[i]) for i in range(len(capital))]
        capital_profit.sort()
        heap = []
        i = 0
        while k:
            while i < len(capital_profit) and capital_profit[i][0] <= w:
                heappush(heap, -capital_profit[i][1])
                i+=1
            if not heap:
                break

            w -= heappop(heap)
            k-=1
            
        return w