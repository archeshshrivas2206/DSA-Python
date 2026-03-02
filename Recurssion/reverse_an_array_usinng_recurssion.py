arr=[1,2,3,4,5,6,7,8,9,10]

left=int(input("enetr left index"))
right=int(input("enetr right index"))

def reverser(arr,l,r):
    if l>=r:
        return
    arr[l],arr[r]=arr[r],arr[l]
    reverser(arr,l+1,r-1)
    return arr
print(reverser(arr,left,right))
    



