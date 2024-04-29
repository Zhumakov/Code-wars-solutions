# https://www.codewars.com/kata/5629db57620258aa9d000014
def mix(s1, s2):
    d1 = {}
    d2 = {}

    for i in s1:
        if i.isalpha() and i.islower():
            d1[i] = d1.get(i, '') + i

    for i in s2:
        if i.isalpha() and i.islower():
            d2[i] = d2.get(i, '') + i

    shared_d = d1 | d2

    res_l = []
    for i in shared_d:
        x = d1.get(i, '')
        y = d2.get(i, '')

        m_len = max(len(x), len(y))
        if m_len > 1:
            if len(x) > len(y):
                res_l.append(f'1:{x}')

            elif len(x) < len(y):
                res_l.append(f'2:{y}')

            else:
                res_l.append(f'=:{x}')

    # First, sort by number of letters, then by line number (there will be a '=' sign at the very end), then by letter
    res_l1 = sorted(res_l, key=lambda x: (len(x[2:-1]), -ord(x[0]), -ord(x[-1])), reverse=True)

    out = '/'.join(res_l1)
    return out
