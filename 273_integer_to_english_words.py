class Solution:
    def numberToWords(self, num: int) -> str:
        def convert_three_digits(three_digits):
            first_digit = three_digits // 100
            two_digits = three_digits % 100
            second_digit = two_digits // 10
            third_digit = two_digits % 10
            lst_third_digit = ["One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
            lst_second_digit = ["Ten", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
            # print(three_digits, two_digits, third_digit)
            builder = []
            if first_digit > 0:
                builder.append(lst_third_digit[first_digit - 1])
                builder.append("Hundred")
            if two_digits == 0:
                pass
            else:
                if two_digits < 10:
                    builder.append(lst_third_digit[third_digit - 1])
                elif 10 < two_digits < 20: # 11-19
                    lst = ["Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
                    builder.append(lst[third_digit - 1])
                elif third_digit == 0: # ten twenty thirty fourty
                    builder.append(lst_second_digit[second_digit - 1])
                else: # x1 - x9
                    builder.append(lst_second_digit[second_digit - 1])
                    builder.append(lst_third_digit[third_digit - 1])

            return " ".join(builder)

        if num == 0:
            return "Zero"
        lst_units = ["Thousand", "Million", "Billion", "Trillion"]
        builder = []
        unit_idx = 0
        while num > 0:

            last_three = num % 1000
            if last_three:
                builder.append(convert_three_digits(last_three))
            else:
                if builder:  # 1M != One million thousand
                    builder.pop()
            num //= 1000

            if num > 0:
                builder.append(lst_units[unit_idx])
                unit_idx += 1

        return " ".join(reversed(builder))

"""
one two three four five six seven eight nine 
ten eleven twelve thirdteen fourteen fifteen sixteen seventeen eighteen nineteen
twenty twenty one

thousand million billion trillion

1 000 010
"""