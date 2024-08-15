class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        freq = {}
        for i in bills:
            if i in freq:
                freq[i] += 1
            else:
                freq[i] = 1
            if i == 10:
                if 5 in freq and freq[5]:
                    freq[5] -= 1
                else:
                    return False
            if i == 20:
                if 5 in freq and 10 in freq and freq[5] and freq[10]:
                    freq[5] -= 1
                    freq[10] -= 1
                elif 5 in freq and freq[5] >= 3:
                    freq[5] -= 3
                else:
                    return False

        return True
