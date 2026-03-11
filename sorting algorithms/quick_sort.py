arr=[9,5,1,3,7,4,6,8,2]

def partition(arr,low,high):
    pivot=arr[low]
    i=low
    j=high
    while i<j:
        while arr[i]<=pivot and i<=high-1:
            i+=1
        while arr[j]>=pivot and j>=low+1:
            j-=1
        if i<j:
            arr[i],arr[j]=arr[j],arr[i]
    arr[low],arr[j]=arr[j],arr[low]
    return j 
def quick_sort_ascending(arr,low,high):
    if low<high:
        p_index=partition(arr,low,high)
        quick_sort_ascending(arr,low,p_index-1)
        quick_sort_ascending(arr,p_index+1,high)
quick_sort_ascending(arr,0,len(arr)-1)
print(arr)


        
