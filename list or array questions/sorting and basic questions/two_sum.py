nums=[5,9,1,2,4,15,6,3]
target=13
def bruteforce(nums,target):
    for i in range(0,len(nums)-1):
        for j in range (i+1,len(nums)):
            if nums[i]+nums[j]==target:
                return [i,j]
            
print("this is bruteforce",bruteforce(nums,target))


def optimal(nums,target):
    n=len(nums)
    freq={}
    for i in range(0,n):
        complement=target-nums[i]
        if complement in freq:
            return [freq[complement],i]
        else:
            freq[nums[i]]=i
print(optimal(nums,target))

