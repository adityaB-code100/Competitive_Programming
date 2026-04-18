def hartals(test_cases):
    results = []

    for case in test_cases:
        days, parties, h_values = case

        lost_days = set()

        for h in h_values:
            for day in range(h, days + 1, h):
                if day % 7 not in (6, 0):
                    lost_days.add(day)

        results.append(len(lost_days))

    return results


test_cases = [
    (14, 3, [3, 4, 8]),   # First case
    (100, 4, [12, 15, 25, 40])  # Second case
]


results = hartals(test_cases)


for res in results:
    print(res)

#OUTPUT
#5
#15