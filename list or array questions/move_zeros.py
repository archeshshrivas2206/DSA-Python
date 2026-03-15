#from a given list/array we have to move the 0's at the end of array while keeeping the other elements in the same order and doing the operation in the starting array only 


nums=[1,0,2,4,3,0,0,3,5,1]
n=len(nums)
def bruteforce(nums,n):
    temp=[]
    for i in range (0,n):
        if nums[i]!=0:
            temp.append(nums[i])
    for j in range(0,len(temp)):
        nums[j]=temp[j]
    for k in range(len(temp),n):
        nums[k]=0
#bruteforce(nums,n)
print(nums)

def optimal(nums,n):
    if len(nums)==1:
        return 1 
    i=0
    while i<len(nums):
        if nums[i]==0:
            break
        i+=1
    if i==len(nums):
        return
    j=i+1
    while j<len(nums):
        if nums[j]!=0:
            nums[i],nums[j]=nums[j],nums[i]
            i+=1
        j+=1
optimal(nums,n)
print(nums)



        

