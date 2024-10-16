class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        heap = [(-a, 'a'), (-b, 'b'), (-c, 'c')]
        heapify(heap)
        s = []
        
        while heap:
            n, c = heappop(heap)
            if len(s) > 1 and s[-1] == c and s[-2] == c:
                if len(heap) == 0:
                    break
                x, y = heappop(heap)
                heappush(heap, (n, c))
                n, c = x, y
            if n == 0:
                break
            s.append(c)
            n += 1
            if n != 0:
                heappush(heap, (n, c))
        
        return ''.join(s)