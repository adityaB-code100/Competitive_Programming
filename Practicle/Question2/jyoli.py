
def jyolly(n,nums):
    flag=True
    for i in range(1,n):
        temp=abs(nums[i]-nums[i-1])

        if temp not in nums:
            flag=False
            break
    
    if flag==True:
        print("Jyolly")
    else:
        print("Not Jyolly")


jyolly(4,[1,4,2,3])
jyolly(5,[1,4,2,-1,6])

# OUTPUT
# Jyolly
# Not Jyolly