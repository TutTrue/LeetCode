class Solution:
    def nthUglyNumber(self, n: int) -> int:
        primes = [2,3,5]
        uglyHeap = [1]
        visited = set()
        visited.add(1)
        for _ in range(n):
            cur = heappop(uglyHeap)
            for prime in primes:
                new_ugly = cur * prime
                if new_ugly not in visited:
                    heappush(uglyHeap, new_ugly)
                    visited.add(new_ugly)
        return cur