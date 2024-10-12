class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        start, end = [], []
        for s, e in intervals:
            start.append(s)
            end.append(e)

        start.sort()
        end.sort()

        j, i = 0, 0
        res = 0
        while i < len(intervals):
            if start[i] > end[j]:
                j+=1
            else:
                i+=1
            res = max(res, i - j)
        return res
                