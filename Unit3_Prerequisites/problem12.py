
def power(s):
    count=0
    for c in s:
        if c=="a":
            count+=1

    print(count)



ls=["abcd",
"aaaa",
"ababab"]

for k in ls:
    power(k)



# OUTPUT
# 1
# 4
# 3

