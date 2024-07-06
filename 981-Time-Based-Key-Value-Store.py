class TimeMap:

    def __init__(self):
        self.dic =  defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.dic[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.dic:
            return ""
        l = self.dic[key]
        i = bisect_left(l, (timestamp,))
        if i < len(l) and l[i][0] == timestamp:
            return l[i][1]
        elif i > 0:
            return l[i - 1][1]
        else:
            return ""


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)