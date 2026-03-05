nums=[4,5,8,2,7,9,1,3,6]

def insertion_sort_ascending(nums):
    n=len(nums)
    for i in range (1,n):
        key=nums[i]
        j=i-1
        while j>=0 and nums[j]>key:
            nums[j+1]=nums[j]
            j-=1
        nums[j+1]=key
def insertion_sort_descending(nums):
    n=len(nums)
    for i in range (1,n):
        key=nums[i]
        j=i-1
        while j>=0 and nums[j]<key:
            nums[j+1]=nums[j]
            j-=1
        nums[j+1]=key

insertion_sort_ascending(nums)
print('ascending order= ',nums)
insertion_sort_descending(nums)
print('ascending order= ',nums)


