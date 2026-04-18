# 9. Reverse and Add UVA 10018

def is_palindrome(n):
    return str(n) == str(n)[::-1]


def reverse_add(n):
    count = 0

    while not is_palindrome(n):
        rev = int(str(n)[::-1])
        n = n + rev
        count += 1

    return count, n


# Given test case
nums = [195, 265, 750]

for num in nums:
    steps, result = reverse_add(num)
    print(steps, result)



# OUTPUT
# 4 9339
# 5 45254
# 3 6666