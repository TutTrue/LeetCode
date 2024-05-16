class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def euclidean_distance(x, y):
            return math.sqrt(x**2 + y**2)

        distences = []
        for x, y in points:
            heappush(distences,(-euclidean_distance(x, y), [x, y]))
            if len(distences) > k:
                heappop(distences)
        res = []
        for _, arr in distences:
            res.append(arr)
        return res