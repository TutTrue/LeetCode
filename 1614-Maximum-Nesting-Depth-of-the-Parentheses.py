class Solution:
    def maxDepth(self, s: str) -> int:
        stack = deque()
        m = 0
        for i in s:
            if i == '(':
                stack.append(i)
            if i == ')':
                m = max(m, len(stack))
                stack.pop()
        return m
        