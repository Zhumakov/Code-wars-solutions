# https://www.codewars.com/kata/53f40dff5f9d31b813000774
def recover_secret(triplets):
    all_letters = set([x for y in triplets for x in y])
    res = ''
    while all_letters:
        for letter in all_letters:
            buffer = []
            for triplet in triplets:
                if letter in triplet:
                    buffer.append(triplet)

            # If an element comes first in all triplets, then it is the next letter in the result
            if all(map(lambda x: x[0] == letter, buffer)):
                res += letter
                all_letters.remove(letter)
                for x in buffer:
                    x.pop(0)
                break
    return res
