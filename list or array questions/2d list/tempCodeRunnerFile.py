def bruteforce(nums):
    r=len(nums)
    c=len(nums[0])

    result=[[0]*c for _ in range(r)]

    n=c

    for i in range(r):
        for j in range(c):
            result[i][j]=nums[(n-1)-j][i]
    matrix_printer(result)

bruteforce(nums)