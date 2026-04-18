#6. Mother Bear UVA 10945
def mother(s):

    if s=="DONE":
        return 
    s=s.lower()
    sc=""
    for c in s:
        if "a"<=c<="z":
            sc+=c

    result=""

    for c in sc:
        result=c+result

    if result==sc:
        print("You won't be eaten!")
    else:
        print("Uh oh..")


ls=["Madam, Im adam!",
"Roma tibi subito motibus ibit amor.",
"Me so hungry!",
"Si nummi immunis",
"DONE"]

for l in ls:
    mother(l)

# OUTPUT
# You won't be eaten!
# You won't be eaten!
# Uh oh..
# You won't be eaten!