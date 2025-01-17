class Solution:
    def doesValidArrayExist(self, derived: List[int]) -> bool:
        res = 0
        for i in range(len(derived) - 1):
            if derived[i] != 0:
                res ^= 1
        if derived[-1] == 0 and res == 0 or derived[-1] == 1 and res == 1:
            return True
        return False
