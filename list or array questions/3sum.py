nums=[-1,0,1,2,-1,-4]


def bruteforce(nums):
    result=set()
    for i in range(len(nums)-2):
        for j in range(i+1,len(nums)-1):
            for k in range(j+1,len(nums)):
                if nums[i]+nums[j]+nums[k]==0 :
                    temp=[nums[i],nums[j],nums[k]]
                    temp.sort()
                    result.add(tuple(temp))
                    

    return result

# print(bruteforce(nums))

def better(nums):
    result=set()
    for i in range(len(nums)):
        myset=set()
        for j in range(i+1,len(nums)):
            third=-(nums[i]+nums[j])
            if third in myset:
                temp=[nums[i],nums[j],third]
                temp.sort()
                result.add(tuple(temp))
            myset.add(nums[j])

    return result
print("the triplet found by the better approach",better(nums))







 


