class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        n=len(prices)
        stack=[n-1]
        res=[x for x in prices]
        for i in range(n-2, -1, -1):
            while stack and prices[i]<prices[stack[-1]]:
                stack.pop()
            if stack: res[i]-=prices[stack[-1]]
            stack.append(i)
        return res