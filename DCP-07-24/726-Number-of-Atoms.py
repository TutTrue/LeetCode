class Solution:
    def countOfAtoms(self, formula: str) -> str:
        stack = [defaultdict(int)]
        i = 0

        while i < len(formula):
            if formula[i] == '(':
                stack.append(defaultdict(int))
            elif formula[i] == ')':
                cur_map = stack.pop()
                cnt = []
                while i+1 < len(formula) and formula[i+1].isdigit():
                    cnt.append(formula[i+1])
                    i+=1
                cnt = 1 if cnt == [] else int(''.join(cnt))
                for k, v in cur_map.items():
                    stack[-1][k] += v * cnt

            else:
                el = formula[i]
                if i + 1 < len(formula) and formula[i+1].islower():
                    el+= formula[i+1]
                    i+=1
                cnt = []
                while i+1 < len(formula) and formula[i+1].isdigit():
                    cnt.append(formula[i+1])
                    i+=1
                cnt = 1 if cnt == [] else int(''.join(cnt))
                stack[-1][el] += cnt
            i+=1
        res = []
        for k in sorted(stack[-1].keys()):
            cnt = \\ if stack[-1][k] == 1 else str(stack[-1][k])
            res.append(k+cnt)
        return ''.join(res)