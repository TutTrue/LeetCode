class Solution:
    def lengthAfterTransformations(self, s: str, t: int) -> int:
        q = deque([0] * 26)
        for c in s:
            q[ord(c) - ord('a')] += 1
        for _ in range(t):
            q.appendleft(q.pop())
            q[1] += q[0]
        return sum(q) % 1000000007