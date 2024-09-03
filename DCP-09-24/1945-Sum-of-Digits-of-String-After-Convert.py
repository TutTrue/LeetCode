class Solution:
    def getLucky(self, s: str, k: int) -> int:
        convert = {
            'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6,
            'g': 7, 'h': 8, 'i': 9, 'j': 1, 'k': 2, 'l': 3,
            'm': 4, 'n': 5, 'o': 6, 'p': 7, 'q': 8, 'r': 9,
            's': 10, 't': 2, 'u': 3, 'v': 4, 'w': 5, 'x': 6,
            'y': 7, 'z': 8
        }
        total = 0
        k -= 1
        for c in s:
            total+= convert[c]

        while k > 0 and total > 9:
            num = 0
            while total > 0:
                num += total % 10
                total //= 10
            total = num
            k-=1
        return total