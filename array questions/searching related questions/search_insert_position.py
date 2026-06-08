nums=[1,3,4,5,8,9,14,15,19,20,21]
target=int(input("mention the element you want to insert "))

def bruteforce(nums,target):
    for i in range(len(nums)):
        if nums[i]>=target:
            return i
    return len(nums)
print("using bruteforce ", bruteforce(nums,target))


def optimal(nums,target):
    lowerbound=len(nums)
    low=0
    high=len(nums)-1
    while low<=high:
        mid=(high+low)//2
        if nums[mid]>=target:
            high=mid-1
            lowerbound=mid
        elif nums[mid]<target:
            low=mid+1
    
        
    return lowerbound
print("by optimal approach",optimal(nums,target))

    

        
        


# def self_done(nums):
#     low=0
#     high=len(nums)-1
#     for i in range(len(nums)):
#         mid=(high+low)//2
#         if mid==target:
#             return 
#         elif mid<target:
#             low=mid+1
#         elif mid>target:
#             high=mid-1