class CustomStack:

    def __init__(self, maxSize: int):
        self.s = [-1] * maxSize
        self.top = -1

    def push(self, x: int) -> None:
        if self.top == len(self.s) - 1:
            return

        self.top+=1
        self.s[self.top] = x

    def pop(self) -> int:
        if self.top == -1:
            return -1
        self.top -= 1
        return self.s[self.top + 1]

    def increment(self, k: int, val: int) -> None:
        for i in range(min(k, self.top+1)):
            self.s[i] += val


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)
