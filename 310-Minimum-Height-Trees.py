class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]
        
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        q = deque()
        
        for node in graph:
            if len(graph[node]) == 1:
                q.append(node)
        
        remaining_nodes = n
        while remaining_nodes > 2:
            remaining_nodes -= len(q)
            for _ in range(len(q)):
                node = q.popleft()
                neighbor = graph[node].pop()
                graph[neighbor].remove(node)
                if len(graph[neighbor]) == 1:
                    q.append(neighbor)
        
        return list(q)
                
# {
#     0: 3
#     1: 3
#     2: 3
#     3: 0, 1, 2, 4
#     4: 3, 5
#     5: 4
# }
