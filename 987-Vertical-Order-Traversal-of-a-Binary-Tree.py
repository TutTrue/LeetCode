class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        n = len(deck)
        deck.sort()
        q = deque(range(n))
        res = [0] * n

        for card in deck:
            res[q.popleft()] = card
            if q:
                q.append(q.popleft())

        return res