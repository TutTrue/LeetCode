class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        s = set()
        removed = set()
        for w in s1.split():
            if w in removed:
                continue
            if w in s:
                s.remove(w)
                removed.add(w)
            else:
                s.add(w)
        for w in s2.split():
            if w in removed:
                continue
            if w in s:
                removed.add(w)
                s.remove(w)
            else:
                s.add(w)
        return s