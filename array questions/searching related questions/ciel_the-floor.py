nums=[3,4,4,4,8,9,9,10,12,12,14,15]

target=int(input("enter the no. "))

def self(nums,target):
    lower=-1
    low=0
    high=len(nums)-1
    result=[]
    while low <= high:
        mid=(high+low)//2
        if nums[mid]==target:
            result.append(nums[mid])
            return result
        elif nums[mid]>target:
            high=mid-1
            lower=mid
        else:
            low=mid+1
    result.append(nums[lower-1])
    result.append(nums[lower])
    return result

print("self solved way ", self(nums,target))
