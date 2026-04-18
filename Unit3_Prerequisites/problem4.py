
#4. All in All UVA 10340
def subsequence(s, t):
    i = 0  # pointer for s

    for ch in t:
        if i < len(s) and ch == s[i]:
            i += 1

    if i == len(s):
        print("Yes")
    else:
        print("No")

s=["sequence subsequence",
"person compression",
"VERDI vivaVittorioEmanueleReDiItalia",
"caseDoesMatter CaseDoesMatter"]


for c in s:
    c=c.split(" ")
    subsequence(c[0],c[1])

# OUTPUT
# Yes
# No
# Yes
# No