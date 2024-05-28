# https://www.codewars.com/kata/51e056fe544cf36c410000fb
import re
from collections import Counter


def top_3_words(text):
    text = re.sub(r'[#/.,:;?!_-]', ' ', text)
    print(text)
    amounts = Counter(text.lower().split())
    amounts = sorted(amounts.items(), key=lambda y: y[1], reverse=True)
    print(amounts)

    i = 0
    res = []
    while len(res) < 3 and i < len(amounts):
        x = amounts[i][0]
        x = re.sub(r"'", '', x)
        if x.isalpha():
            res.append(amounts[i][0])
        i += 1

    print(res)
    return res
