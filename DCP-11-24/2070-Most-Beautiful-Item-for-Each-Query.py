class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        res = []
        items.sort()
        cur_max = 0
        max_arr = [0]
        for p, b in items:
            cur_max = max(cur_max, b)
            max_arr.append(cur_max)
        for q in queries:
            i = bisect_right(items, q, key=itemgetter(0))
            res.append(max_arr[i])

        return res