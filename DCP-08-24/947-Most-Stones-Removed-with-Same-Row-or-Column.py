class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        graph = {}
        for x, y in stones:
            if x not in graph:
                graph[x] = []
            if ~y not in graph:
                graph[~y] = []
            graph[x].append(~y)
            graph[~y].append(x)
        
        visited = set()
        
        def dfs(node):
            stack = [node]
            while stack:
                current = stack.pop()
                if current not in visited:
                    visited.add(current)
                    for neighbor in graph[current]:
                        if neighbor not in visited:
                            stack.append(neighbor)
        
        components = 0
        for x, y in stones:
            if x not in visited:
                dfs(x)
                components += 1
        
        return len(stones) - components
