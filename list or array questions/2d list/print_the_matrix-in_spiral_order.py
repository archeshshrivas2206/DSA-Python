nums=[[1,2,3,4,5,6],[20,21,22,23,24,7],[19,32,33,34,25,8],[18,31,36,35,26,9],[17,30,29,28,27,10],[16,15,14,13,12,11]]

def onlysolution(nums):
    result =[]
    if not nums or not nums[0]:
        return result
    n=len(nums)
    top=0
    left=0
    bottom=n-1
    right=n-1
    while top<=bottom and left <=right:

        for i in range(left,right+1):
            result.append(nums[top][i])
        top+=1
        for i in range(top,bottom+1):
            result.append(nums[i][right])
        right-=1
        if top<=bottom:
            for i in range(right,left-1,-1):
                result.append(nums[bottom][i])
            bottom-=1
        if left<=right:
            for i in range(bottom,top-1,-1):
                result.append(nums[i][left])
            left+=1
    return result

print(onlysolution(nums))

        


    

    
    
            



