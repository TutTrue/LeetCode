class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        q = deque(nums)

        while len(q) > 1:
            for _ in range(len(q)):
                q.append((q.popleft() + q[0]) % 10)
            q.pop()

        return q[0]
