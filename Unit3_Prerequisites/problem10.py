#10. Word Scramble UVA 483
lines = [
    "I love you.",
    "You love me.",
    "We're a happy family."
]

for line in lines:
    words = line.split()
    reversed_words = []

    for word in words:
        reversed_words.append(word[::-1])

    print(" ".join(reversed_words))

# OUTPUT
# I evol .uoy
# uoY evol .em
# er'eW a yppah .ylimaf