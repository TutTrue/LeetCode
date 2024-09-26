class MyCalendar:

    def __init__(self):
        self.li = []

    def book(self, start: int, end: int) -> bool:
        tmp =[start, end]
        for e in self.li:
            if self.overlap(e, tmp):
                return False
        self.li.append(tmp)
        return True

    def overlap(self, a, b):
        return a[0] < b[1] and b[0] < a[1]

# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)