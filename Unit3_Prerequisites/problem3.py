#3. WERTYU UVA 10082
def decode(s):
    s=s.lower()


    decode_map = {
        '1': '`', '2': '1', '3': '2', '4': '3', '5': '4',
        '6': '5', '7': '6', '8': '7', '9': '8', '0': '9',
        '-': '0', '=': '-',

        'w': 'q', 'e': 'w', 'r': 'e', 't': 'r', 'y': 't',
        'u': 'y', 'i': 'u', 'o': 'i', 'p': 'o', '[': 'p',
        ']': '[', '\\': ']',

        's': 'a', 'd': 's', 'f': 'd', 'g': 'f', 'h': 'g',
        'j': 'h', 'k': 'j', 'l': 'k', ';': 'l', "'": ';',

        'x': 'z', 'c': 'x', 'v': 'c', 'b': 'v', 'n': 'b',
        'm': 'n', ',': 'm', '.': ',', '/': '.'," ":" "
    }





    result=""
    for c in s:
        result=result+decode_map[c] 

    
    print(result.upper())

decode("O S, GOMR YPFSU/")


# OUTPUT
# I AM FINE TODAY.