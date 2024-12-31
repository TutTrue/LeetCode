class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        days_set = set(days)
        @lru_cache(maxsize=None)
        def rec(day):
            if day > 365:
                return 0

            if day not in days_set:
                return rec(day + 1)

            cost_1 = costs[0] + rec(day + 1)
            cost_7 = costs[1] + rec(day + 7)
            cost_30 = costs[2] + rec(day + 30)

            return min(cost_1, cost_7, cost_30)
        return rec(days[0])