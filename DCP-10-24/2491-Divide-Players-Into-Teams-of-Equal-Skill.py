class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        total = sum(skill)
        total = (2 * total) // len(skill)
        l, r = 0, len(skill) - 1
        res = 0
        while r > l:
            if skill[r] + skill[l] != total:
                print(total, skill[r], skill[l])
                return -1
            res += (skill[r] * skill[l])
            l += 1
            r-= 1
        return res