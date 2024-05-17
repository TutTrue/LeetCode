class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        trans = str.maketrans(order, ascii_lowercase)
        twords = [w.translate(trans) for w in words]
        return sorted(twords) == twords
