class Solution:
    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
        res = []
        row, col = len(land), len(land[0])

        def dfs(i, j, l):
            if i == row or j == col or land[i][j] != 1:
                return

            land[i][j] = 0
            l[-1] = j
            l[-2] = max(l[-2], i)
            dfs(i+1, j, l)
            dfs(i, j+1, l)

        
        for i in range(len(land)):
            for j in range(len(land[i])):
                if land[i][j] == 1:
                    l = [i, j, i, j]
                    dfs(i, j, l)
                    res.append(l)
        return res