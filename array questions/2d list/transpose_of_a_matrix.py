nums=[[1,2,3],[4,5,6],[7,8,9]]

rows=len(nums)
column=len(nums[0])

empty_matrix= [ [0]*rows for _ in range (column)] 

for i in range(rows):
    for j in range(column):
        empty_matrix[i][j]=nums[j][i]
print(empty_matrix)

