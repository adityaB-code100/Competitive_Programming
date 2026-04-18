# 5. Simply Emirp UVA 10235
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


nums = [17, 18, 19, 179, 199]

for n in nums:
    if not is_prime(n):
        print(f"{n} is notprime.")
    else:
        rev = int(str(n)[::-1])
        if rev != n and is_prime(rev):
            print(f"{n}is emirp.")
        else:
            print(f"{n}is prime.")





# output
# 17is emirp.
# 18 is notprime.
# 19is prime.
# 179is emirp.
# 199is emirp.