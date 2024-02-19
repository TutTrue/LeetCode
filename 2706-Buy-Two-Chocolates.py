class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        prices.sort()
        after = money - (prices[0] + prices[1])
        return  after if after >= 0 else money