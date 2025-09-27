class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        res = 0
        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                for k in range(j + 1, len(points)):
                    a = points[i]
                    b = points[j]
                    c = points[k]
                    res = max(
                        res,
                        0.5
                        * abs(
                            a[0] * (b[1] - c[1])
                            + b[0] * (c[1] - a[1])
                            + c[0] * (a[1] - b[1])
                        ),
                    )

        return res
