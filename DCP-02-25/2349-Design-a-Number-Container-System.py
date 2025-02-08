class NumberContainers:

    def __init__(self):
        self.map={}
        self.valIdx=defaultdict(SortedSet)

    def change(self, index: int, number: int) -> None:
        if index in self.map:
            if self.map[index]==number: 
                return 
            preVal=self.map[index]
            self.valIdx.get(preVal).remove(index)
        
        self.valIdx[number].add(index)
        self.map[index]=number

    def find(self, number: int) -> int:
        if number not in self.valIdx or not self.valIdx[number]:
            return -1
        return self.valIdx[number][0]

# Your NumberContainers object will be instantiated and called as such:
# obj = NumberContainers()
# obj.change(index,number)
# param_2 = obj.find(number)