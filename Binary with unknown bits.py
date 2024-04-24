def average_to_binary(n):
    """For a better understanding of this kata, you should also read the other kata at the link
     https://www.codewars.com/kata/64348795d4d3ea00196f5e76"""
    # Handling special cases
    if n == 0:
        return ['0']
    elif n == 0.5:
        return ['x']
    elif n == 1:
        return ['1']

    average = bin(int(n)).lstrip('0b')

    # Determine the minimum possible number
    min_num = '1' + '0' * (len(average) - 1)

    output = set()
    for i in range(int(n), int(min_num, 2) - 1, -1):
        current = bin(i).lstrip('0b')
        # We determine the opposite number, i.e. a number located at the same distance from n as the current one
        end = bin(int(n + (n - i))).lstrip('0b')

        # If the lengths of their binary records do not match, then there are no more suitable pairs of numbers
        if len(current) != len(end):
            break

        # Rez should produce a string
        # where the average between the maximum possible number and the minimum possible number is n
        rez = ''
        for j in range(len(current)):
            if current[j] == end[j]:
                rez += current[j]
            else:
                rez += 'x'

        # If you only get numbers, add x instead of the first number to comply with the kata rule
        if 'x' not in rez:
            rez = 'x' + rez[1:]

        # Any sequence will have 2 spelling options
        output.add(rez)
        output.add('x' + rez[1:])

    return list(output)