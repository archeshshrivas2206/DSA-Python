a=int(input("enter the no. of rotation you want :"))
arr=[1,2,3,4,5,6,7,8,9]
n=len(arr)
def right_rotator(arr):
    for k in range(0,a):
        temp=arr[n-1]
        for i in range(n-2,-1,-1):
            arr[i+1]=arr[i]
        arr[0]=temp
right_rotator(arr)
print("the array after rotation will be : ",arr)