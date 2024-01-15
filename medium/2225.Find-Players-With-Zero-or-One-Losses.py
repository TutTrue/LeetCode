# 2225. Find Players With Zero or One Losses

class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        dic =defaultdict(int)
        _0match = set()
        _1match = []

        for win, lose in matches:
            dic[lose] += 1
            _0match.add(win)

        for k, v in dic.items():
            if v == 1:
                _1match.append(k)
            if v >= 1 and k in _0match:
                _0match.remove(k)

        _1match.sort()

        return [sorted(list(_0match)), _1match]
