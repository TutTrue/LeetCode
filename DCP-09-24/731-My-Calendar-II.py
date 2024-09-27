class MyCalendarTwo:

    def __init__(self):
        self.over = []
        self.non_over = []

    def book(self, start: int, end: int) -> bool:
        for s, e in self.over:
            if end > s and e > start:
                return False

        for s, e in self.non_over:
            if end > s and e > start:
                self.over.append((max(start, s), min(end, e)))
        self.non_over.append((start, end))
        return True

# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(start,end)