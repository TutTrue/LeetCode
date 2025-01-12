class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        if len(s) % 2 != 0: 
            return False
        balance = 0
        for char, lock in zip(s, locked):
            if lock == '0' or char == '(':
                balance += 1
            elif char == ')':
                balance -= 1
            if balance < 0:
                return False
        balance = 0
        
        for char, lock in zip(reversed(s), reversed(locked)):
            if lock == '0' or char == ')':
                balance += 1
            elif char == '(':
                balance -= 1
            if balance < 0:
                return False
        return True
