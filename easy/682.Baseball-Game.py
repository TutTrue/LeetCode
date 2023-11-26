# 682. Baseball Game

class Solution(object):
    def calPoints(self, operations):
        """
        :type operations: List[str]
        :rtype: int
        """
        stack = []

        for i in operations:
            if i == '+':
                stack.append(stack[-1] + stack[-2])
            elif i == 'D':
                stack.append(stack[-1] * 2)
            elif i == 'C':
                stack.pop()
            else:
                stack.append(int(i))
        x = 0
        x = sum(int(i) for i in stack)
        return x
