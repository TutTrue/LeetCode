class Solution:
    def customSortString(self, order: str, s: str) -> str:
        dic = {char: index for index, char in enumerate(order)}
        return ''.join(sorted(s, key=lambda x: dic.get(x, float('inf'))))
        