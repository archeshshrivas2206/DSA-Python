nums=[1,99,101,98,2,5,3,100,1,1]
def bruteforce(nums):
    n=len(nums)
    max_count=0
    for i in range(0,n):
        num=nums[i]
        count=1
        while num+1 in nums:
            count+=1
            num+=1
        max_count=max(max_count,count)
    return max_count
print("Bruteforce ", bruteforce(nums))

def better(nums):
    nums.sort()
    last_smallest=float("-inf")
    count=0
    maxcount=0
    for i in nums:
        if i ==last_smallest+1:
            count+=1
            maxcount=max(maxcount,count)
            last_smallest=i

        elif i!=last_smallest:

            count=1
        last_smallest=i
    return maxcount
print("better ",better(nums))

def optimal(nums):
    new_set=set()
    for i in nums:
        new_set.add(i)
    longest=0
    count=0
    for i in new_set:
        if i-1 not in new_set:
            num=i
            count=1
            while num+1 in new_set:
                count+=1
                num+=1
            longest=max(longest,count)
    return longest
print("optimal",optimal(nums))


    