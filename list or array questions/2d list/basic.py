#A 2d list is basically a list within a list 
nums=[[1,2,3],[4,5,6],[7,8,9]]
for i in range(0,len(nums)):
    print(len(nums[i]))
print()

#how to iterate each element of 2d array
rows=len(nums)
column=len(nums[0])
for i in range(rows):
   for j in range(column):
       print(nums[i][j],end=" ")
   print()
print()
#simple questions 
#print the upper triangle
for i in range(0,len(nums)):
    for j in range(0,len(nums[0])):
        if j>=i:
            print(nums[i][j],end=' ')
        else: 
            print(end="  ")
    print()
#print lower triangle

for i in range(0,len(nums)):
    for j in range(0,len(nums[0])):
        if j<=i:
            print(nums[i][j],end=" ")
        else:
            print(end='  ')
    print()
print()

## only diagonal

for i in range(0,len(nums)):
    for j in range(0,len(nums[0])):
        if j==i:
            print(nums[i][j],end=' ')
        else:
            print(end='  ')
    print()

