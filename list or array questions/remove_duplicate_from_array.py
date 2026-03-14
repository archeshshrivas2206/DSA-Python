arr=[9,9,1,3,5,5,7,4,4,6,6,8,8,2,2]
dictionary={}
def duplicate_finder_bruteforce(arr):
    for i in range(0,len(arr)):
            dictionary[arr[i]]=0
    j=0    
    for k in dictionary:
        arr[j]=k
        j+=1
    del arr[j:]
    return j
print(duplicate_finder_bruteforce(arr))
print(arr)

def duplicate_finder_optimal(arr):#two pointer approach 
    i=0
    j=1
    while j<len(arr):
        if arr[i]==arr[j]:
            j+=1
        else:
            i+=1
            arr[i],arr[j]=arr[j],arr[i]
    del arr[i+1:]
    return i+1
print(duplicate_finder_optimal(arr))
print(arr)


