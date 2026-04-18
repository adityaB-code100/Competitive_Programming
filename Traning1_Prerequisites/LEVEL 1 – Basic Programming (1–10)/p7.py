#7.	Reverse a Number

n=int(input("n"))


num=0
while n>0:
    r=n%10
    num=num*10+r
    n=n//10
    


print(num)

