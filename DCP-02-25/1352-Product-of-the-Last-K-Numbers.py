class ProductOfNumbers:

    def __init__(self):
        self.li = []
        self.prod = 1

    def add(self, num: int) -> None:
        if num == 0:
            self.li = []
            self.prod =1
        else:
            self.prod *= num
            self.li.append(self.prod)

    def getProduct(self, k: int) -> int:
        if len(self.li) < k: return 0
        if len(self.li) == k: return self.li[-1]
        return self.li[-1] // self.li[-k-1]


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)