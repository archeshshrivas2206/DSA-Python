nums=[5,9,1,2,4,15,6,3]
target=13
def bruteforce(nums):
    for i in range(0,len(nums)-1):
        for j in range (i+1,len(nums)):
            if nums[i]+nums[j]==target:
                return [i,j]
            
print(bruteforce(nums))


def optimal(nums):
    n=len(nums)
    