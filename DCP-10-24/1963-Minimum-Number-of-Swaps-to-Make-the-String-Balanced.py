class Solution:
    def minSwaps(self, s: str) -> int:
        stack = []
        for c in s:
            if len(stack) > 0 and c == ']' and stack[-1] == '[':
                stack.pop()
            else:
                stack.append(c)

        n = len(stack) // 2
        if n % 2 == 1:
            n += 1
        return n // 2