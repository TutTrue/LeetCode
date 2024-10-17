class Solution:
    def maximumSwap(self, num: int) -> int:
        num = list(str(num))
        max_i=-1
        max_digit='0'
        swap_i = swap_j = -1
        for i in range(len(num) - 1, -1, -1):
            if num[i] > max_digit:
                max_digit = num[i]
                max_i = i
            if num[i] < max_digit:
                swap_i = i
                swap_j = max_i
        num[swap_i], num[swap_j] = num[swap_j], num[swap_i]
        return int(''.join(num))