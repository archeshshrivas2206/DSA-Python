num=[2,4,7,6,5,3,1,8,9]

def bubble_sort_ascending(num):
    n=len(num)
    swapped=False
    for i in range(n):
        for j in range(0,n-i-1):
            if num[j]>num[j+1]:
                num[j],num[j+1]=num[j+1],num[j]
                swapped=True
        if swapped==False:
            break
def bubble_sort_descending(num):
    n=len(num)
    for i in range (n):
        for j in range(0,n-i-1):
            if num[j+1]>num[j]:
                num[j],num[j+1]=num[j+1],num[j]
                swapped=True
        if swapped==False:
            break


bubble_sort_ascending(num)
print(num)

bubble_sort_descending(num)
print(num)
