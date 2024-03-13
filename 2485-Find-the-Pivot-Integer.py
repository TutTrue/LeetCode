class Solution:
    def pivotInteger(self, n: int) -> int:
        e = n * (n + 1) // 2
        s = n
        i = n
        while e > s:
            s += i - 1
            e -= i
            i-=1
        return i if e == s else -1

    def pivotIntegerMath(self, n: int) -> int:
        sum = n * (n + 1) // 2
        a = math.sqrt(sum)
        return int(a) if a - math.ceil(a) == 0 else -1
