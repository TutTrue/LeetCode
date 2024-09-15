class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        vowels = 'eioau'
        mask = 0
        mask_idx = {0: -1}
        res = 0

        for i, c in enumerate(s):
            if c in vowels:
                mask = mask ^ (1 + ord(c) - ord('a'))
            if mask in mask_idx:
                res = max(res, i - mask_idx[mask])
            else:
                mask_idx[mask] = i
        return res
