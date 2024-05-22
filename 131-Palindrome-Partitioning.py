class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def is_palindrome(sub):
            s, e = 0, len(sub) - 1
            while e >= s:
                if sub[e] != sub[s]:
                    return False
                e-=1
                s+=1
            return True
        def backtrack(start, path):
            if start == len(s):
                result.append(path[:])
                return
            for end in range(start + 1, len(s) + 1):
                if is_palindrome(s[start:end]):
                    backtrack(end, path + [s[start:end]])

        result = []
        backtrack(0, [])
        return result
