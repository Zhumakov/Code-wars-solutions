"""Solution for kata https://www.codewars.com/kata/53f40dff5f9d31b813000774"""

from time import perf_counter


TIMEOUT = 1


def recover_secret(triplets):
    all_letters = set([letter for triplet in triplets for letter in triplet])
    res = ''
    start = perf_counter()
    while all_letters:
        end = perf_counter()
        if end - start > TIMEOUT:
            raise TimeoutError

        for letter in all_letters:
            buffer = []
            for triplet in triplets:
                if letter in triplet:
                    buffer.append(triplet)

            # If an element comes first in all triplets, then it is the next letter in the result
            if all(map(lambda x: x[0] == letter, buffer)):
                res += letter
                all_letters.remove(letter)
                for triplet in buffer:
                    triplet.pop(0)
                break
    return res
