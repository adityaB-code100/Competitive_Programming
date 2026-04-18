#8.	Palindrome Number

n=int(input("n"))


temp=n

num=0
while n>0:
    r=n%10
    num=num*10+r
    n=n//10
    

if temp==num:

    print("Palindrom No")
else:
    print("Not Palindrom No")

