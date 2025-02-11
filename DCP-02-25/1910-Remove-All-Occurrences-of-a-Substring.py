class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        stack = []
        part = list(part)
        for c in s:
            stack.append(c)
            while len(stack) >= len(part) and stack[-len(part):] == part:
                for _ in range(len(part)):
                    stack.pop()

        return ''.join(stack)