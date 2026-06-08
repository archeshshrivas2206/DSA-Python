arr=[9,5,1,3,7,4,6,8,2]
nums=[1,2,3,4,5,6,7,8,9]
def sorted_array_finder(arr):
    for i in range (0,len(arr)-2):
        if arr[i]>arr[i+1]:
            return False
        
print(sorted_array_finder(arr))
print(sorted_array_finder(nums))