class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        g = {i for i in range(n)}

        for _, i in edges:
            if i in g:
                g.remove(i)

        return -1 if len(g) != 1 else list(g)[0]