nums=[1,1,1,2,3,3,5,6,7,7,7,9,12,12,13]



target=int(input("enter the target"))
def selff(nums,target):
    lb=-1
    low=0
    high=len(nums)-1
    while low<=high:
        mid=(high+low)//2
        if nums[mid]>=target:
            high=mid-1
            lb=mid
        elif nums[mid]<target:
            low=mid+1
    return lb
print(selff(nums,target))
