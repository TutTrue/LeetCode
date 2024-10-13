class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        ordered = []
        for k, num_list in enumerate(nums):
            for n in num_list:
                ordered.append((n, k))
        ordered.sort()

        i, k = 0, 0
        ans = []
        count = defaultdict(int)

        for j in range(len(ordered)):
            if count[ordered[j][1]] == 0:
                k += 1
            count[ordered[j][1]] += 1

            if k == len(nums):
                while count[ordered[i][1]] > 1:
                    count[ordered[i][1]] -= 1
                    i += 1
                if not ans or ans[1] - ans[0] > ordered[j][0] - ordered[i][0]:
                    ans = [ordered[i][0], ordered[j][0]]

        return ans