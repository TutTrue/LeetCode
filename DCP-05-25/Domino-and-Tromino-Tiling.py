class Solution:
    def numTilings(self, n: int) -> int:
        if n == 1 or n == 2:
            return n
        if n == 3: return 5
        q = deque([1, 2, 5])
        for i in range(n - 3):
            q.append(q[-1] * 2 + q[0])
            q.popleft()
        
        return q[-1] % (10**9 + 7)