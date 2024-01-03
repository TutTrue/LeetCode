# 2125. Number of Laser Beams in a Bank

class Solution(object):
    def numberOfBeams(self, bank):
        """
        :type bank: List[str]
        :rtype: int
        """
        res = 0
        row = 0
        prev = 0
        while prev < len(bank) and bank[prev].count('1') == 0:
            prev+=1
        row = prev+1
        while row < len(bank):
            if bank[row].count('1') == 0:
                row+=1
                continue
            res += bank[prev].count('1') * bank[row].count('1')
            prev = row
            row+=1
        return res
