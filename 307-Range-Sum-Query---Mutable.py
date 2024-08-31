class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.n = len(nums)
        self.blockSize = math.ceil(math.sqrt(self.n))
        self.blocks = [0] * self.blockSize

        for i in range(self.n):
            self.blocks[i // self.blockSize] += nums[i]


    def update(self, index: int, val: int) -> None:
        blockIndex = index // self.blockSize
        self.blocks[blockIndex] += val - self.nums[index]
        self.nums[index] = val


    def sumRange(self, l: int, r: int) -> int:
        s = 0
        startBlock = l // self.blockSize
        endBlock = r // self.blockSize

        if startBlock == endBlock:
            for i in range(l, r + 1):
                s += self.nums[i]
        else:
            for i in range(l, (startBlock + 1) * self.blockSize):
                s += self.nums[i]
            for i in range(startBlock + 1, endBlock):
                s += self.blocks[i]
            for i in range(endBlock * self.blockSize, r + 1):
                s += self.nums[i]

        return s


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)