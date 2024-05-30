class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        a = 0
        count = 0
        for i in range(len(arr)):
            a = 0
            for j in range(i, len(arr)):
                a ^= arr[j]
                if a == 0:
                    count+=j - i
        return count