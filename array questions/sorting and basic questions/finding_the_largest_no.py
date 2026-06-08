arr= [55,32,-97,99,3,67]

def largest_no_finder_method1(arr):
    largest=arr[0]
    for i in range(0,len(arr)):
        if arr[i]>largest:
            largest=arr[i]
    return largest
print ("largest element is ", largest_no_finder_method1(arr))

def largest_no_finder_method2(arr):#minus infinity method 
    largest=float("-inf")#way to write minus infinity
    for i in range (0,len(arr)):
        largest= max(largest,arr[i])#this way max function gives O(1) complexity
    return largest
print ("largest element is ", largest_no_finder_method1(arr))





        

