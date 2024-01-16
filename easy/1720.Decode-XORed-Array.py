# 1720. Decode XORed Array

class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        res = [first] * (len(encoded) + 1)
        for i in range(len(encoded)):
            res[i+1] = encoded[i] ^ res[i]
        return res
