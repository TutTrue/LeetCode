class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        ops = {
            '+': lambda x, y: x + y,
            '-': lambda x, y: x - y,
            '*': lambda x, y: x * y
        }

        def backtrack(l, r):
            res = []

            for i in range(l, r+1):
                op = expression[i]
                if op in ops:
                    nums1 = backtrack(l, i-1)
                    nums2 = backtrack(i+1, r)

                    for n1 in nums1:
                        for n2 in nums2:
                            res.append(ops[op](n1, n2))
            if res == []:
                res.append(int(expression[l:r+1]))

            return res

        return backtrack(0, len(expression) - 1)
