value_map = {
    '2':2, '3':3, '4':4, '5':5, '6':6,
    '7':7, '8':8, '9':9, 'T':10,
    'J':11, 'Q':12, 'K':13, 'A':14
}


def get_hand_rank(hand):
    values = sorted([value_map[c[0]] for c in hand], reverse=True)
    suits = [c[1] for c in hand]

    # Count occurrences
    counts = {}
    for v in values:
        counts[v] = counts.get(v, 0) + 1

    count_values = sorted(counts.values(), reverse=True)
    unique_vals = sorted(counts.keys(), reverse=True)

    is_flush = len(set(suits)) == 1
    is_straight = (values == list(range(values[0], values[0]-5, -1)))

    # Special case A-2-3-4-5
    if values == [14,5,4,3,2]:
        is_straight = True
        values = [5,4,3,2,1]

    # Ranking
    if is_straight and is_flush:
        return (8, values)
    elif 4 in count_values:
        return (7, unique_vals)
    elif 3 in count_values and 2 in count_values:
        return (6, unique_vals)
    elif is_flush:
        return (5, values)
    elif is_straight:
        return (4, values)
    elif 3 in count_values:
        return (3, unique_vals)
    elif count_values.count(2) == 2:
        return (2, unique_vals)
    elif 2 in count_values:
        return (1, unique_vals)
    else:
        return (0, values)


def compare_hands(black, white):
    rank_b = get_hand_rank(black)
    rank_w = get_hand_rank(white)

    if rank_b > rank_w:
        return "Black wins."
    elif rank_w > rank_b:
        return "White wins."
    else:
        return "Tie."



inputs = [
    "2H 3D 5S 9C KD 2C 3H 4S 8C AH",
    "2H 4S 4C 2D 4H 2S 8S AS QS 3S",
    "2H 3D 5S 9C KD 2C 3H 4S 8C KH",
    "2H 3D 5S 9C KD 2D 3H 5C 9S KH"
]

# Run
for line in inputs:
    cards = line.split()
    black = cards[:5]
    white = cards[5:]
    print(compare_hands(black, white))


# output
# White wins.
# Black wins.
# Black wins.
# Tie.