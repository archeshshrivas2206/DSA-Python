nums=[-2,1,-3,4,-1,2,1,-5,4]

def bruteforce(nums):
    n= len(nums)
    maxi=float("-inf")
    count=float("-inf")
    for i in range(n):
        count=0
        for j in range (i,n):
            count=count+nums[j]
            maxi=max(maxi,count)
    return maxi
print("By brute force ", bruteforce(nums))


def optimal(nums):#kadaen's Algoritm 
    total=0
    maxi=float("-inf")
    for i in range (len(nums)):
        if total<0:
            total=0
        else:
            total=total+nums[i]
            maxi=max(maxi,total)
    return maxi
print("By optimal ",optimal(nums))
