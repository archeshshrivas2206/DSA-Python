nums=[9,3,5,2,6,7,1,8,4]
n=len(nums)
def selection_sort_ascending(nums):
    for i in range(0,n):
        minindex= i
        for j in range (i+1,n):
            if nums[j]<nums[minindex]:
                minindex=j
        nums[i],nums[minindex]=nums[minindex],nums[i]
def selection_sort_descending(nums):
    for i in range (n-1,-1,-1):
        minindex=i
        for j in range(i-1,-1,-1):
            if nums[j]<nums[minindex]:
                minindex=j
        nums[i],nums[minindex]=nums[minindex],nums[i]


selection_sort_ascending(nums)
print("ascending order sort ",nums)
selection_sort_descending(nums)
print("descending order sort ",nums)


