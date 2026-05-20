nums=[9,5,1,3,7,4,6,8,2]
target=int(input("Enter the value you want to search "))
for i in range(0,len(nums)):
    if nums[i]==target:
        print("Element fouond at ",i," index ")
    print("Element not in the array ")
