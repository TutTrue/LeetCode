class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        result = []

        if (numerator < 0) ^ (denominator < 0):
            if numerator != 0:
                result.append("-")

        numerator, denominator = abs(numerator), abs(denominator)

        integer_part, remainder = divmod(numerator, denominator)
        result.append(str(integer_part))

        if remainder == 0:
            return "".join(result)

        result.append(".")

        seen = {}
        while remainder != 0:
            if remainder in seen:
                start = seen[remainder]
                result.insert(start, "(")
                result.append(")")
                break

            seen[remainder] = len(result)
            remainder *= 10
            digit, remainder = divmod(remainder, denominator)
            result.append(str(digit))

        return "".join(result)
