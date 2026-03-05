arr=[3,5,9,7,2,8,1,4,6]
def merge_array(l,r):
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
    if i<n:
        while i<n:
            result.append(l[i])
            i+=1
    else:
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
    


    