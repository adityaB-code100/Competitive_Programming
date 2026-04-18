	#Prime Number Check
import math
n=int(input("n"))


flag=True
if n&1 or n==2:
    
    for i in range(3,int(math.sqrt(n)),+2):
        if n%i==0:
            print("Not Prime")
            flag=False
            break
    
    if flag:
        print("Prime")
else:
    print("Not Prime")