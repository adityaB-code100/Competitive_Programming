# 8. Common Permutation UVA 10252
def common_permutation(a, b):
    result = ""

    for ch in "abcdefghijklmnopqrstuvwxyz":
        result += ch * min(a.count(ch), b.count(ch))

    return result


# Given test input
inputs = [
    "pretty", "women",
    "walking", "down",
    "the", "street"
]

# Process pairs
for i in range(0, len(inputs), 2):
    a = inputs[i]
    b = inputs[i + 1]
    print(common_permutation(a, b))



# output
# e
# nw
# et