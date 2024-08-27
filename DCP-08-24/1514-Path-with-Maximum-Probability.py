class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        dist = [-float('inf')] * n
        adj = defaultdict(list)

        for i, edge in enumerate(edges):
            u, v = edge
            adj[u].append((v, succProb[i]))
            adj[v].append((u, succProb[i]))
        
        pq = [(-1, start_node)] 
        dist[start_node] = 0

        while pq:
            prob, node = heapq.heappop(pq)
            prob = -prob
            if node == end_node:
                return prob
            for neighbor, cost in adj[node]:
                newProb = prob * cost
                if newProb > dist[neighbor]:
                    dist[neighbor] = newProb
                    heapq.heappush(pq, (-newProb, neighbor))
        
        return 0