"""Solution for kata https://www.codewars.com/kata/54b72c16cd7f5154e9000457"""
CODE = {'A': '.-',     'B': '-...',   'C': '-.-.',
        'D': '-..',    'E': '.',      'F': '..-.',
        'G': '--.',    'H': '....',   'I': '..',
        'J': '.---',   'K': '-.-',    'L': '.-..',
        'M': '--',     'N': '-.',     'O': '---',
        'P': '.--.',   'Q': '--.-',   'R': '.-.',
        'S': '...',    'T': '-',      'U': '..-',
        'V': '...-',   'W': '.--',    'X': '-..-',
        'Y': '-.--',   'Z': '--..',

        '0': '-----',  '1': '.----',  '2': '..---',
        '3': '...--',  '4': '....-',  '5': '.....',
        '6': '-....',  '7': '--...',  '8': '---..',
        '9': '----.'
        }
CODE = {v: k for k, v in CODE.items()}


def get_speed(bits):
    counter = 0
    switcher = bits[0]
    possible_speed = 1
    for i in bits:
        if i == switcher:
            counter += 1

        elif i != switcher:
            # If the sequence of ones cannot be a dash
            if switcher == '1' and counter % 3 != 0:
                return counter
            if switcher == '1' and counter % 3 == 0:
                possible_speed = counter

            # If a sequence of zeros cannot be a pause between characters and between words
            elif switcher == '0' and counter % 3 != 0 and counter % 7 != 0:
                return counter

            counter = 1
            switcher = i

    return possible_speed


def decode_bits(bits):
    # Remove extra zeros
    bits = bits.strip('0')

    # To process the last units
    bits += '00'

    # Getting speed
    speed = get_speed(bits)

    switcher = bits[0]
    counter = 0
    out = ''
    for i in bits:

        if i == switcher:
            counter += 1

        # When interrupting a sequence of characters, use its length and type
        elif i != switcher:
            counter /= speed

            if switcher == '1' and counter == 1:
                out += '.'
            elif switcher == '1' and counter == 3:
                out += '-'

            elif switcher == '0' and counter == 3:
                out += ' '
            elif switcher == '0' and counter == 7:
                out += '   '

            counter = 1
            switcher = i

    return out


def decode_morse(morse_code):
    words = morse_code.split('   ')
    words = [word.split(' ') for word in words]
    out_words = []
    print(words)
    for word in words:
        buffer = []
        for letter in word:
            buffer.append(CODE[letter])
        out_words.append(''.join(buffer))

    return ' '.join(out_words)