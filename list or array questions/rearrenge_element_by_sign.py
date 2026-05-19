nums=[5,10,-3,-1,-10,6]

def bruteforce(nums):
    positive=[]
    negative=[]
    for i in range (0,len(nums)):
        if nums[i]>=0:
            positive.append(nums[i])
        else:
            negative.append(nums[i])
    for i in range (0,len(positive)):
        nums[2*i]=positive[i]
        nums[2*i+1]=negative[i]
    return nums
print("Brute Force",bruteforce(nums))

def optimal(nums):
    n=len(nums)
    result=[0]*n
    i=0
    j=1
    for k in range(0,len(nums)):
        if nums[k]>=0:
            result[i]=nums[k]
            i+=2
        else:
            result[j]=nums[k]
            j+=2
    return result
print("Optimal",optimal(nums))