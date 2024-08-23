from fractions import Fraction

class Solution:
    def fractionAddition(self, expression: str) -> str:
        s=\\
        num=eval(expression)
        num1=int(num)
        if num1==num:
            s=str(num1)
            s+='/1'
        else:
            res=Fraction(num).limit_denominator()
            print(res)
            s=str(res)
        return s
