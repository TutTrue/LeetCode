class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        def remove_pair(pair, score):
            nonlocal s

            stack = []
            res = 0
            for c in s:
                if c == pair[1] and stack and stack[-1] == pair[0]:
                    stack.pop()
                    res += score
                else:
                    stack.append(c)
            s = ''.join(stack)
            return res
        pair = 'ab' if x > y else 'ba'
        return remove_pair(pair, max(x, y)) + remove_pair(pair[::-1], min(x, y))