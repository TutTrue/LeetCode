class Solution:\r
    def wonderfulSubstrings(self, word: str) -> int:\r
        ans = 0\r
        prefix = 0  \r
        count = [0] * 1024  \r
        count[0] = 1  \r
\r
        for c in word:\r
          prefix ^= 1 << ord(c) - ord('a')\r
          ans += count[prefix]\r
          ans += sum(count[prefix ^ 1 << i] for i in range(10))\r
          count[prefix] += 1\r
\r
        return ans