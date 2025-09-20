class Router:

    def __init__(self, memoryLimit: int):
        self.memoryLimit = memoryLimit
        self.q = deque()
        self.dup = set()
        self.dest_map = defaultdict(list)


    def addPacket(self, source: int, destination: int, timestamp: int) -> bool:
        packet = (source, destination, timestamp)
        if packet in self.dup:
            return False

        self.q.append(packet)
        self.dup.add(packet)
        ts_list = self.dest_map[destination]
        idx = bisect_right(ts_list, timestamp)
        ts_list.insert(idx, timestamp)

        if len(self.q) > self.memoryLimit:
            old = self.q.popleft()
            self.dup.remove(old)
            ts_list = self.dest_map[old[1]]
            idx = bisect_left(ts_list, old[2])
            ts_list.pop(idx)

        return True

    def forwardPacket(self) -> List[int]:
        if not self.q:
            return []
        p = self.q.popleft()
        self.dup.remove(p)
        ts_list = self.dest_map[p[1]]
        idx = bisect_left(ts_list, p[2])
        ts_list.pop(idx)
        return list(p)

    def getCount(self, destination: int, startTime: int, endTime: int) -> int:
        ts_list = self.dest_map[destination]
        if not ts_list:
            return 0
        left = bisect_left(ts_list, startTime)
        right = bisect_right(ts_list, endTime)
        return right - left


# Your Router object will be instantiated and called as such:
# obj = Router(memoryLimit)
# param_1 = obj.addPacket(source,destination,timestamp)
# param_2 = obj.forwardPacket()
# param_3 = obj.getCount(destination,startTime,endTime)
