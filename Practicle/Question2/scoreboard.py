def contest_scoreboard(inputs):
    data = {}

    for line in inputs:
        if line.strip() == "":
            continue

        c, p, time, status = line.split()
        c = int(c)
        p = int(p)
        time = int(time)

        if c not in data:
            data[c] = {
                "solved": 0,
                "penalty": 0,
                "wrong": {},
                "solved_problems": set()
            }

        if status == 'C':
            if p not in data[c]["solved_problems"]:
                data[c]["solved"] += 1
                data[c]["penalty"] += time + 20 * data[c]["wrong"].get(p, 0)
                data[c]["solved_problems"].add(p)

        elif status == 'I':
            if p not in data[c]["solved_problems"]:
                data[c]["wrong"][p] = data[c]["wrong"].get(p, 0) + 1

    result = []
    for c in data:
        result.append((c, data[c]["solved"], data[c]["penalty"]))

    result.sort(key=lambda x: (-x[1], x[2], x[0]))

    for r in result:
        print(r[0], r[1], r[2])

inputs = [
    "1 2 10 I",
    "3 1 11 C",
    "1 2 19 R",
    "1 2 21 C",
    "1 1 25 C"
]

contest_scoreboard(inputs)


# OUTPUT
# 1 2 66
# 3 1 11