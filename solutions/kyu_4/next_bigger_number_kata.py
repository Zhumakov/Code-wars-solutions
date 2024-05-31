"""Solution for kata https://www.codewars.com/kata/55983863da40caa2c900004e."""


def find_nearest_bigger(n):
    num_str = list(str(n))
    for i in range(-1, -len(num_str) - 1, -1):
        for j in range(-1, i, -1):
            if num_str[i] < num_str[j]:
                num_str[i], num_str[j] = num_str[j], num_str[i]
                return num_str, i
    return None, None


def next_bigger(n):
    num_str, i = find_nearest_bigger(n)
    if num_str is None:
        return -1

    res = num_str[-len(num_str):i + 1] + sorted(num_str[i + 1:])

    return int(''.join(res))
