class TaskManager:

    def __init__(self, tasks: List[List[int]]):
        self.heap = []
        self.deleted = defaultdict(int)
        self.task_dict = {}

        for userId, taskId, priority in tasks:
            heappush(self.heap, (-priority, -taskId, userId))
            self.task_dict[taskId] = (-priority, userId)

    def add(self, userId: int, taskId: int, priority: int) -> None:
        heappush(self.heap, (-priority, -taskId, userId))
        self.task_dict[taskId] = (-priority, userId)

    def edit(self, taskId: int, newPriority: int) -> None:
        userId = self.task_dict[taskId][1]
        self.deleted[(self.task_dict[taskId][0], -taskId, userId)] += 1
        self.task_dict[taskId] = (-newPriority, userId)

        heappush(self.heap, (-newPriority, -taskId, userId))

    def rmv(self, taskId: int) -> None:
        self.deleted[
            (self.task_dict[taskId][0], -taskId, self.task_dict[taskId][1])
        ] += 1

    def execTop(self) -> int:
        if not self.heap: return -1
        task = heappop(self.heap)
        while task in self.deleted and self.deleted[task] > 0:
            self.deleted[task] -= 1
            if not self.heap: return -1
            task = heappop(self.heap)
        return task[2] if task else -1


# Your TaskManager object will be instantiated and called as such:
# obj = TaskManager(tasks)
# obj.add(userId,taskId,priority)
# obj.edit(taskId,newPriority)
# obj.rmv(taskId)
# param_4 = obj.execTop()
