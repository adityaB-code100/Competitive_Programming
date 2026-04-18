def largest(nums):

    maxi=float("-inf")

    for num in nums:
        maxi=max(maxi,num)

    return maxi

def secondlarge(nums):
    nums.sort(reverse=True)

    return  nums[1] if len(nums)>=2 else "No second latrget element"


def reversearry(nums):
    n=len(nums)
    left,right=0,n-1
    while left<right:
        nums[left],nums[right]=nums[right],nums[left]
        left+=1
        right-=1

    return nums


def rotate(nums,k):
    n=len(nums)
    
    for _ in range(k%n):
        temp=nums[0]

        for i in range(1,n):
            nums[i-1]=nums[i]

        nums[n-1]=temp

    
    return nums


def countFrequency(nums):
    my_dict={

    }

    for num in nums:
        if num not in my_dict:
             my_dict[str(num)]=0
        my_dict[str(num)]+=1

    
    return my_dict

def removeduplicate(nums):
    my_dict={

    }

    for num in nums:
        if num not in my_dict:
             my_dict[num]=0
        my_dict[num]+=1

    
    return list(my_dict.keys())



def reversestring(s):
    result=""
    for c in s:
        result=c+result
    
    return result
    

def palindromstring(s):
    result=""
    for c in s:
        result=c+result
    
    return result==s
    

def Vowels(s):
    Vowel={"a","e","i","o","u"}
    s.lower()

    vow=0
    const=0

    for c in s:
        if c in Vowel:
            vow+=1
        else:
            const+=1
        
    
    return {"Vowel":vow, "Consonent":const}

def anagram(s1,s2):
    def countFrequency(s):
        my_dict={

        }

        for c in nums:
            if c not in my_dict:
                my_dict[c]=0
            my_dict[c]+=1

        return my_dict
    
    if countFrequency(s1)==countFrequency(s2):
        return "anagram"
    else:
        return "NOt ANagram"

s="Frequency"
nums=[2,6,4,8,9,4,6,7,2,1]

s1="triangle"
s2="integral"




print("Largest no ",largest(nums))
print("Second largets ",secondlarge(nums))
print("Reverse Arry",reversearry(nums))
print("Rotate arry by k postion",rotate(nums,3))
print("Frequency count",countFrequency(nums))
print("Remove Duplicate",removeduplicate(nums))
print("Reverse String : ",reversestring(s))

print("String is Palindrome : ",palindromstring(s))
print("Vowel and Consonent : ",Vowels(s))

print("ANagram or not : ",anagram(s1,s2))

