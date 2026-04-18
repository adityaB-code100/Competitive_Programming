
#5.	Fibonacci Series (n terms)

n=int(input("n"))

a=0
b=1

for i in range(0,n):
    print(a)
    a, b = b, a + b


