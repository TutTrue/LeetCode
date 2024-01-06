# 1235. Maximum Profit in Job Scheduling

class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        job = list(zip(startTime, endTime, profit))
        job.sort()
        startTime.sort()

        memo = {}
        memo[len(startTime)] = 0 # base case if i == len(startTime) return 0
        def rec(i, memo=memo):
            if i in memo:
                return memo[i]
            j = bisect_left(startTime, job[i][1])
            # take the job or not
            one = job[i][2] + rec(j) # take the job
            two = rec(i+1) # take the next job
            memo[i] = max(one, two)
            return memo[i]
        return rec(0)
