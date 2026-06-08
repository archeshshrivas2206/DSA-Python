#merge two sorted array such that every element in the merged array is distinct 

nums=[1,1,1,2,4,6,7]
arr=[1,2,3,6,7,8,9,10]

def optimal(nums,arr):
    result=[]
    i=0
    j=0
    while i<(len(nums)) and j<(len(arr)):
        if nums[i]<=arr[j]:
            if len(result)==0 or result[-1]!=nums[i]:
                result.append(nums[i])
            i+=1
        else:
            if arr[j]<nums[i]:
                if len(result)==0 or result[-1]!=arr[j]:
                    result.append(arr[j])
                j+=1
    while i<j:
        if len(result)==0 or result[-1]!=nums[i]:
            result.append(nums[i])
        i+=1
    while j<i:
        if len(result)==0 or result[-1]!=arr[j]:
            result.append(arr[j])
        j+=1
    print(result)

optimal(nums,arr)                