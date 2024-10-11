class Solution:
    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:
        chairs = [-1] * len(times)
        cur_time = 1
        target = times[targetFriend]
        times.sort()
        for arrival, leaving in times:
            cur_time = arrival
            i = 0
            while chairs[i] != -1 and chairs[i] > cur_time:
                i+=1
            if arrival == target[0]:
                return i
            chairs[i] = leaving
        return -1