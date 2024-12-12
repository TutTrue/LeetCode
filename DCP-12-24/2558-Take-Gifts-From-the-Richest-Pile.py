class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        for i in range(len(gifts)):
            gifts[i] *= -1

        heapify(gifts)
        for i in range(k):
            heappush(gifts, -math.floor(math.sqrt(-heappop(gifts))))

        return sum(gifts) * -1