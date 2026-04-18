def threen(k,j):   
        def logic(n):
                l=1
                while n>1:
                    if n&1==0:
                        n=n//2
                    else:
                        n=3*n+1
                    l+=1
            
                return l
        maxi=0

        for i in range(k,j+1):
            maxi=max(logic(i),maxi)
        print(k," ",j," ",maxi)

threen(1,10)
threen(100,200)
threen(201,210)
threen(900,1000)

# OUTPUT
# 1   10   20
# 100   200   125
# 201   210   89
# 900   1000   174
