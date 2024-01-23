class Solution:
    def maxLength(self, arr: List[str]) -> int:
        res = [0]
        def isUnique(s):
            return len(s) == len(set(s))
        def dfs(i, curString):
            if isUnique(curString):
                res[0] = max(res[0], len(curString))
            else:
                return
            if i == len(arr):
                return

            for idx in range(i, len(arr)):
                dfs(idx+1, curString+arr[idx])
        dfs(0, "")
        return res[0]
