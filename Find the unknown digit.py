# https://www.codewars.com/kata/546d15cebed2e10334000ed9
import re


def solve_runes(runes):
    known_digit = set(re.findall(r'\d', runes))

    # If you cannot substitute a zero, skip it
    start = 0
    validate = re.findall(r'([^\d]|\b)?\d+', runes)
    if validate:
        start += 1

    for i in range(start, 10):
        # The question mark can only contain a number that is not in the original expression.
        if str(i) in known_digit:
            continue

        # We replace all question marks with numbers, we get the first number, the second and the result
        expression = re.sub(r'\?', str(i), runes)
        expression, result = expression.split('=')

        if eval(expression) == eval(result):
            return i
    return -1
