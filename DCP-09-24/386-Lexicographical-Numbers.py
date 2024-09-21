class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        res = []

        def dfs(i):
            if i > n:
                return
            res.append(i)
            for j in range(10):
                dfs(i * 10 + j)
        for i in range(1, 10):
            dfs(i)
        return res