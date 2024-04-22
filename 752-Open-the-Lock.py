class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        def children(lock):
            res = []
            for i in range(4):
                res.append(lock[:i] + str((int(lock[i]) + 1) % 10) + lock[i+1:])
                res.append(lock[:i] + str((int(lock[i]) - 1 + 10) % 10) + lock[i+1:])
            return res
        visited = set(deadends)
        if "0000" in visited:
            return -1
        q = deque()
        q.append(["0000", 0])
        while q:
            lock, turn = q.popleft()
            if lock == target:
                return turn
            for i in children(lock):
                if i not in visited:
                    visited.add(i)
                    q.append([i, turn + 1])
        return -1