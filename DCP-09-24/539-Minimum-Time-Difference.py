class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        times = [0] * len(timePoints)
        for i, time in enumerate(timePoints):
            times[i] = int(time[:2]) * 60 + int(time[3:])

        times.sort()
        m = float('inf')
        for i in range(1, len(times)):
            m = min(m, times[i] - times[i-1])
        m = min(m, 1440 - times[-1] + times[0])
        return m