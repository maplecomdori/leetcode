class Solution:
    def isNumber(self, s: str) -> bool:
        def is_integer(string):
            if not string:
                return False

            if string[0] in ['+', '-']:
                return string[1:].isdigit()
            else:
                return string.isdigit()

        def is_decimal(string):
            if not string:
                return False

            if string[0] in ['+', '-']:
                string = string[1:]
            if not string:
                return False
            if string[:-1].isdigit() and string[-1] == '.':
                return True
            if string[0] == '.' and string[1:].isdigit():
                return True
            decimal_index = string.find('.')
            if string[:decimal_index].isdigit() and string[decimal_index + 1:].isdigit():
                return True
            return False

        def is_exponent(string):
            if not string:
                return False
            return string[0] in ['e', 'E'] and is_integer(string[1:])

        def is_valid(string):
            e_index = string.find('e')
            E_index = string.find('E')

            index = max(e_index, E_index)
            if index == -1:
                return is_integer(string) or is_decimal(string)
            else:
                return (is_integer(string[:index]) or is_decimal(string[:index])) and is_exponent(string[index:])

        return is_valid(s)


"""
2
0089
-0.1
+3.14
4.
-.9
2e10
-9E3
3e+7
+6e-1
53.5e93
-123.456e789
#################
abc
1a
1e
e3

"""