#10.	Armstrong Number
n=int(input("n"))




num=0
temp=n
while n>0:
   num+=1
   n=n//10

total=0

n=temp
while n>0:
   r=n%10
   total+=(r**num)
   n=n//10


if temp==total:

    print("Armstong No")
else:
    print("Not Armstong No")

    