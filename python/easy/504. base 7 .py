class Solution:
    def convertToBase7(self, num: int) -> str:
        decimal_num=num
        if decimal_num == 0:
            return "0"

        is_negative = False
        if decimal_num < 0:
            is_negative = True
            decimal_num = abs(decimal_num)

        base7_digits = []
        while decimal_num > 0:
            remainder = decimal_num % 7
            base7_digits.append(str(remainder))
            decimal_num //= 7

        base7_representation = "".join(base7_digits[::-1])

        if is_negative:
            return "-" + base7_representation
        else:
            return base7_representation
