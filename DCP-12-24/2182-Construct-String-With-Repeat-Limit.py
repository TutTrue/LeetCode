class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        res = []
        count = Counter(s)
        heap = [(-ord(c), cnt) for c, cnt in count.items()]
        heapify(heap)
        while heap:
            c1, cnt1 = heappop(heap)
            cnt_added = min(repeatLimit, cnt1)
            res.append(chr(-c1) * cnt_added)
            if cnt_added == cnt1:
                continue
            else:
                cnt1 = cnt1 - cnt_added
            if not heap:
                continue
            c2, cnt2 = heappop(heap)
            res.append(chr(-c2))
            cnt2 -= 1
            if cnt2 != 0:
                heappush(heap, (c2, cnt2))
            heappush(heap, (c1, cnt1))

        return ''.join(res)
