#7. Soundex UVA 10260
def soundex(word):
    mapping = {
        'B': '1', 'F': '1', 'P': '1', 'V': '1',
        'C': '2', 'G': '2', 'J': '2', 'K': '2',
        'Q': '2', 'S': '2', 'X': '2', 'Z': '2',
        'D': '3', 'T': '3',
        'L': '4',
        'M': '5', 'N': '5',
        'R': '6'
    }

    prev = ''
    result = ''

    for ch in word:
        if ch in mapping:
            code = mapping[ch]
            if code != prev:
                result += code
            prev = code
        else:
            prev = ''   # reset on A, E, I, O, U, H, W, Y

    return result


# Given test cases
words = ["KHAWN", "PFISTER", "BOBBY"]

for w in words:
    print(soundex(w))


# OUTPUT
# 25
# 1236
# 11