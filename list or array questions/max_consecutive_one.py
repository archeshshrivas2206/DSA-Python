nums=[1,1,0,1,0,1,1,1,1,0,1,1]

def max_consecutive_one(nums):
    count=0
    max_count=0
    for i in range (0, len(nums)):
        if nums[i]==1:
            count=count+1
        else:
            if count>max_count:
                max_count=count
                count=0
            else:
                count=0
    print("max count is equal to ",max_count)
max_consecutive_one(nums)