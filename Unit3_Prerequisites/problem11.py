# 11. Extend to Palindrome UVA 11475
def is_palindrome(s):
    return s == s[::-1]

def extendpalidrom(s):
    for i in range(len(s)):
        if is_palindrome(s[i:]):
            return s + s[:i][::-1]

ls = ["aaaa", "abba", "amanaplanacanal", "xyz"]

for c in ls:
    print(extendpalidrom(c))

# OUTPUT
# aaaa
# abba
# amanaplanacanalpanama
# xyzyx