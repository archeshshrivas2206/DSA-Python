arr=[3,5,9,7,2,8,1,4,6]
def merge_array_ascending(l,r):
    result=[]
    i,j=0,0
    n,m=len(l),len(r)
    while i<n and j<m:
        if l[i]<=r[j]:
            result.append(l[i])
            i+=1
        else:
            result.append(r[j])
            j+=1
    while i<n:
            result.append(l[i])
            i+=1
    while j<m:
            result.append(r[j])
            j+=1
    return result
def merge_sort_ascending(arr):
    if len(arr)<=1:
        return arr
    mid=len(arr)//2
    left_arr=arr[:mid]
    right_arr=arr[mid:]
    left=merge_sort_ascending(left_arr)
    right=merge_sort_ascending(right_arr)
    return merge_array_ascending(left,right)
def merge_array_descending(l,r):
    result=[]
    n=len(l)
    m=len(r)
    i,j=0,0
    while i<n and j<m:
        if l[i]>=r[j]:
            result.append(l[i])
            i+=1
        else:
            result.append(r[j])
            j+=1

    while i<n:
            result.append(l[i])
            i+=1
    while j<m:
            result.append(r[j])
            j+=1
    return result
def merge_sort_descending(arr):
    if len(arr)<=1:
         return arr
    mid =len(arr)//2
    left_array=arr[:mid]
    right_array=arr[mid:]
    left=merge_sort_descending(left_array)
    right=merge_sort_descending(right_array)
    return merge_array_descending(left,right)
         
        
print(merge_sort_ascending(arr))
print(merge_sort_descending(arr))



    