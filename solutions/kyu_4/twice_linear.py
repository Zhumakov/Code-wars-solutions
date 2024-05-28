# https://www.codewars.com/kata/5672682212c8ecf83e000050
def dbl_linear(n):
    seq = set()
    seq.add(1)
    counter = 2
    while len(seq) <= n:
        if (counter - 1) / 2 in seq or (counter - 1) / 3 in seq:
            seq.add(counter)

        counter += 1
    seq = sorted(list(seq))
    return seq[n]
