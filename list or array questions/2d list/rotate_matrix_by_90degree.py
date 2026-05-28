nums=[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]


def matrix_printer(nums):
    for i in range(len(nums)):
        for j in range(len(nums[i])):
            print(nums[i][j],end="  ")
        print()

matrix_printer(nums)


# def bruteforce(nums):
#     r=len(nums)
#     c=len(nums[0])

#     result=[[0]*c for _ in range(r)]

#     n=c

#     for i in range(r):
#         for j in range(c):
#             result[i][j]=nums[(n-1)-j][i]
#     matrix_printer(result)

# bruteforce(nums)

def optimal(nums):
    n=len(nums)

    #transpose 
    for i in range(n):
        for j in range(i+1,n):
            
            nums[i][j],nums[j][i]=nums[j][i],nums[i][j]
    
    matrix_printer(nums)

    for i in range(n):
        for j in range(len(nums[0])//2):
            nums[i][j],nums[i][n-1-j]=nums[i][n-1-j],nums[i][j]
            

    matrix_printer(nums)


optimal(nums)
