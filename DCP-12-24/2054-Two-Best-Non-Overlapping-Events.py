class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        events.sort(key=lambda x: x[1])

        max_until = []
        max_value = 0
        for _, end, value in events:
            max_value = max(max_value, value)
            max_until.append((end, max_value))

        res = 0
        for start, end, value in events:
            res = max(res, value)

            idx = bisect.bisect_left(max_until, (start, 0)) - 1
            if idx >= 0:
                res = max(res, value + max_until[idx][1])
        return res
