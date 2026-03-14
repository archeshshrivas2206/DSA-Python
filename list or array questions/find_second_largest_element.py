arr=[9,5,1,3,7,4,6,89,2]


def second_largest_finder(arr):#better approach 
    second_largest=float("-inf")
    first_largest=float("-inf")
    for i in range(0,len(arr)):
        first_largest=max(first_largest,arr[i])
    for i in range (0,len(arr)):
        if arr[i]>second_largest and arr[i]!=first_largest:
            second_largest=arr[i]
    return second_largest
print("second largest is ",second_largest_finder(arr))

def second_largest_finder_optimal(arr):#optimal approach 
    second_largest=float("-inf")
    first_largest=float("-inf")
    for i in range(0,len(arr)):
        if arr[i]>first_largest:
            second_largest=first_largest
            first_largest=arr[i]
        elif arr[i]>second_largest and arr[i]!=first_largest:
            second_largest=arr[i]
    return second_largest
print("second largest is ",second_largest_finder(arr),"by optimal way ")
        