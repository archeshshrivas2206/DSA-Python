arr=[1,2,3,4,5,6,7,8,9]
n=len(arr)
k=int(input("Enter the rotations you want"))
rotations=k%n

def right_rotator_by_k_place_bruteforce(arr):#brute force method 
    for _ in range(0,rotations):#one way of doing rotation
        e=arr.pop()
        arr.insert(0,e)

def right_rotator_by_k_place_better(arr):# slicing 
    arr[:]= arr[-rotations:] + arr[:-rotations]

    
def reverser(arr,l,r):
    while l<r:
        arr[l],arr[r]=arr[r],arr[l]
        l+=1
        r-=1

def right_rotator_by_k_place_optimal(arr):
    reverser(n-k,n-1)#reversing the part that is supposed to be rotated and inserted at top
    reverser(0,n-k-1)#reversing the remaining part
    reverser(0,n-1)#reversing the whole array 

