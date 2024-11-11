class Solution:
    def primeSubOperation(self, nums: List[int]) -> bool:
        def is_prime(num):
            for i in range(2, int(sqrt(num)) + 1):
                if num % i == 0:
                    return False

            return True
        prev = 0

        for i in nums:
            upper = i - prev

            largest_prime = 0

            for j in range(upper - 1, 1, -1):
                if is_prime(j):
                    largest_prime = j
                    break

            if i - largest_prime <= prev:
                return False
            prev = i - largest_prime

        return True

            