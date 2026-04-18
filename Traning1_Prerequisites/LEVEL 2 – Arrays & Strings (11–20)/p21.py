'''21.	Frequency of Elements using Map
22.	First Non-Repeating Character
23.	Remove Duplicates using Set
24.	Sort Array using Built-in Function
25.	Sort Strings Lexicographically
26.	Sort Pair / Object based on Second Value
27.	Count Distinct Elements
28.	Intersection of Two Arrays
29.	Union of Two Arrays
30.	Word Frequency Counter'''


#21
def countFrequency(nums):
    my_dict={

    }

    for num in nums:
        if num not in my_dict:
             my_dict[str(num)]=0
        my_dict[str(num)]+=1

    
    return my_dict

#22
def firstnonrepeting(nums):
    my_dict={

    }

    for num in nums:
        if num not in my_dict:
             my_dict[str(num)]=0
        my_dict[str(num)]+=1

    
    for num in nums:
        if my_dict[str(num)]==0:
            return num
    


def removeDuplicate_usingset(nums):
    return list(tuple(set(nums)))


def arrysort(nums):
    return nums.sort()

def sortString(s):
    return sorted(s)

def countditinct(nums):
    return len(list(tuple(set(nums))))

def intersection(nums1,nums2):
    return set(nums1)&set(nums2   )

def unionofarry(nums1,nums2):
    return nums1.union(nums2)
nums1=[2,6,4,8,9,4,6,7,2,1]
nums2=[2,6,4,8,9,4,2,1]
print(intersection(nums1,nums2))
print(unionofarry(set(nums1),set(nums2)))