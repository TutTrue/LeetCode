class Solution:
    def minOperations(self, logs: List[str]) -> int:
        pos = 0
        for log in logs:
            if log == './':
                continue
            elif log == '../':
                if pos:
                    pos-=1
            else:
                pos+=1
        return pos