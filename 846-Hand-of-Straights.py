class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize == 1:
            return False
        freq = {}
        for i in hand:
            freq[i] = freq.get(i, 0) + 1
        hand = list(freq.keys())
        heapify(hand)
        while hand:
            cur = hand[0]
            for i in range(cur, cur+groupSize):
                if i not in freq:
                    return False
                freq[i] -=1
                if freq[i] == 0:
                    if i != hand[0]:
                        return False
                    heappop(hand)
        return True