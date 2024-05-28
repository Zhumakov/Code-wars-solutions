# https://www.codewars.com/kata/51b66044bce5799a7f000003
class RomanNumerals:

    @staticmethod
    def to_roman(val: int) -> str:
        to_r = {1000: 'M', 900: 'CM', 500: 'D', 400: 'CD', 100: 'C', 90: 'XC', 50: 'L', 40: 'XL', 10: 'X', 9: 'IX',
                5: 'V',
                4: 'IV', 1: 'I'}
        res = ''
        while val > 0:
            for num in to_r:
                while val >= num:
                    val -= num
                    res += to_r[num]
        return res

    @staticmethod
    def from_roman(roman_num: str) -> int:
        from_r = {'M': 1000, 'CM': 900, 'D': 500, 'CD': 400, 'C': 100, 'XC': 90, 'L': 50, 'XL': 40, 'X': 10, 'IX': 9,
                  'V': 5, 'IV': 4, 'I': 1}
        roman_num += ' '

        res = 0
        for i in range(len(roman_num) - 1):
            if from_r[roman_num[i]] >= from_r.get(roman_num[i + 1], 0):
                res += from_r[roman_num[i]]
            else:
                res -= from_r[roman_num[i]]

        return res
