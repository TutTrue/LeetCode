class Solution:
    def numberToWords(self, num: int) -> str:
        dict = {
            1: \One\,
            2: \Two\,
            3: \Three\,
            4: \Four\,
            5: \Five\,
            6: \Six\,
            7: \Seven\,
            8: \Eight\,
            9: \Nine\,
            10: \Ten\,
            11: \Eleven\,
            12: \Twelve\,
            13: \Thirteen\,
            14: \Fourteen\,
            15: \Fifteen\,
            16: \Sixteen\,
            17: \Seventeen\,
            18: \Eighteen\,
            19: \Nineteen\,
            20: \Twenty\,
            30: \Thirty\,
            40: \Forty\,
            50: \Fifty\,
            60: \Sixty\,
            70: \Seventy\,
            80: \Eighty\,
            90: \Ninety\,
        }

        result = \\

        if num == 0:
            return \Zero\

        def convert(n):
            if n == 0:
                return \\

            if n in dict:
                return dict[n]

            if n // 1000000000 > 0:
                return (
                    convert(n // 1000000000) + \ Billion \ + convert(n % 1000000000)
                ).strip()

            if n // 1000000 > 0:
                return (
                    convert(n // 1000000) + \ Million \ + convert(n % 1000000)
                ).strip()

            if n // 1000 > 0:
                return (convert(n // 1000) + \ Thousand \ + convert(n % 1000)).strip()

            if n // 100 > 0:
                return (convert(n // 100) + \ Hundred \ + convert(n % 100)).strip()

            if n // 10 > 0:
                return (convert((n // 10) * 10) + \ \ + convert(n % 10)).strip()

            return \\

        return convert(num).strip()
