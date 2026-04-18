def Trip(arr):
        n=len(arr)
        if n==0:
            return

        arr = [int(round(x * 100)) for x in arr]

        avg = sum(arr) 

        result=[0]*n
        ans=0
        for i in range(n):
            result[i]=arr[i]-avg
            if result[i]<0:
                ans+=result[i]        
        print(f"${abs(ans)/100}")

arr=[10.00,20.00,30.00]
Trip(arr)

arr=[15.00,15.01,3.00,3.01]
Trip(arr)

# OutPut
# $10.0
# $11.99