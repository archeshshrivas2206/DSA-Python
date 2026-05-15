#you have to find the missing no. in the list where each no. is represented only once and only 1 no. is missing from the series. 


nums=[1,0,3,4]

def missing_finder_brute(nums):
    n=len(nums)
    for i in range(0,n+1):
        if i not in nums:
            print("the missing no is ",i )
missing_finder_brute(nums)

def missing_finder_better(nums):
    n=len(nums)
    frequency={}
    for i in range(0,n+1) :
        frequency[i]=0
    for i in nums:
        frequency[i]=1
    for k,u in frequency.items():
        if u==0:
            print("missing element is ",k)
missing_finder_better(nums)


def missing_finder_optimal(nums):
    n=len(nums)
    count=0
    for i in range(0,n):
        count=count+nums[i]
    missing=((n*(n+1))//2)-count
    print("the missing no is ",missing )
missing_finder_optimal(nums)