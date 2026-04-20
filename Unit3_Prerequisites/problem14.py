#14. Period UVA 455
def smallest_period(s):
    n = len(s)

    for k in range(1, n + 1):
        if n % k == 0:  # must divide length
            pattern = s[:k]
            if pattern * (n // k) == s:
                return k


s = "HoHoHo"

print(smallest_period(s))

# OUTPUT
# 2