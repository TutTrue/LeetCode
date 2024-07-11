class Solution:
    def reverseParentheses(self, s: str) -> str:
        def reverse(li: List, idx: int):
            s = idx
            while li[s] != '(':
                s-=1
            li[s], li[idx] = li[idx], li[s]
            idx-=1
            s+=1
            while idx >= s:
                li[idx], li[s] = li[s], li[idx]
                idx-=1
                s+=1
            li.pop()

        stack = deque()
        idx = -1
        for c in s:
            if c == ')':
                reverse(stack, idx)
                idx-=1
            else:
                stack.append(c)
                idx+=1
        return ''.join(stack)
        


