import re


class InvalidRomanNumeralError(ValueError):
    pass


class Solution:
    def romanToInt(self, s: str) -> int:
        """convert Roman numeral to integer"""
        s = s.upper()
        roman_numeral_pattern = re.compile("""
        ^                   
        M{0,4}              # Тысячи - 0 до 4
        (CM|CD|D?C{0,3})    # Сотни - 900 (CM), 400 (CD), 0-300 (от 0 до 3 C),
                            #         500-800 (D и от 0 до 3 C)
        (XC|XL|L?X{0,3})    # Десятки - 90 (XC), 40 (XL), 0-30 (от 0 до 3 X),
                            #           50-80 (L и от 0 до 3 X)
        (IX|IV|V?I{0,3})    # Единицы - 9 (IX), 4 (IV), 0-3 (от 0 до 3 I),
                            #           5-8 (V и от 0 до 3 I)
        $                   
        """, re.VERBOSE)

        if not roman_numeral_pattern.search(s):
            raise InvalidRomanNumeralError(f'Sorry {s} is not a valid roman numeral')

        values = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
        n = [values[i] for i in s]
        return sum([value if value >= n[min(index + 1, len(n) - 1)] else -value for index, value in enumerate(n)])

