# https://www.codewars.com/kata/526d84b98f428f14a60008da


def hamming(n):
    i, j, k = 0, 0, 0
    hamming_list = [1]

    for _ in range(n):
        num = min(2 * hamming_list[i], 3 * hamming_list[j], 5 * hamming_list[k])
        hamming_list.append(num)

        if 2 * hamming_list[i] <= num:
            i += 1
        if 3 * hamming_list[j] <= num:
            j += 1
        if 5 * hamming_list[k] <= num:
            k += 1

    return hamming_list[-2]
