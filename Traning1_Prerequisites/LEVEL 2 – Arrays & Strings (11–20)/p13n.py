def mainf(a,b):

    def three1plusone(n):
        count=1
        while n>1:
            if n&1:
                n=n*3+1
            else:
                n=n//2
            count+=1
        return count

    maxi=0
    for i in range(a,b+1):

       maxi=max(three1plusone(i),maxi)

    print(a,"||",b,"||",maxi)
    
print("A","||","B","||","Max Length")

print("="*30)
mainf(1,10)
print("="*30)
mainf(100,200)
print("="*30)

mainf(201,210)
print("="*30)

mainf(900,1000)
print("="*30)
