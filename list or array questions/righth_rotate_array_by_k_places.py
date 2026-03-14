arr=[1,2,3,4,5,6,7,8,9]
n=len(arr)
k=int(input("Enter the rotations you want"))
rotations=k%n
def right_rotator_by_k_place_bruteforce(arr):
    for _ in range(0,rotations):#one way of doing rotation
        e=arr.pop()
        arr.insert(0,e)

def right_rotator_by_k_place_slightlybetter(arr):
    