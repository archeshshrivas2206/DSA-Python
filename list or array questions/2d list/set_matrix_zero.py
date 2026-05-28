nums=[[7,9,2,3],[20,8,0,10],[29,0,-10,5],[4,14,6,7]]

def matrix_printer(nums):
    for i in range(len(nums)):
        for j in range(len(nums[i])):
            print(nums[i][j],end=" ")
        print()

matrix_printer(nums)


def bruteforce_self(nums):
    #traversal
    temp_cord_i=[]
    temp_cord_j=[]

    for i in range(len(nums)):
        for j in range(len(nums[i])):
            if nums[i][j]==0:
                temp_cord_i.append(i)
                temp_cord_j.append(j)
    print("Zero found at ",temp_cord_j,temp_cord_i)

    for i in range(len(nums)):
        for j in range(len(nums[i])):
            if i in temp_cord_i or j in temp_cord_j :
                nums[i][j]=0
            
         
            

bruteforce_self(nums)
matrix_printer(nums)


def optimal(nums):
    r=len(nums)
    c=len(nums[0])

    rowtracker=[0 for _ in range(r)]
    columntracker=[0 for _ in range(c)]

    for i in range(r):
        for j in range(c):
            if nums[i][j]==0:
                rowtracker[i]=-1
                columntracker[j]=-1
    
    for i in range(r):
        for j in range(c):
            if rowtracker[i]==-1 or columntracker[j]==-1:
                nums[i][j]=0


        

    