from array import array

arr=array('i',[6,14,15,16,17,19,20,29,33])

arr.append(48)#adds at the end of the array
print(arr)

a=arr.count(14)#counts the occurrence of given element
print(a)


arr.extend([55,66,77])#adds multiple elements at the end of the array
print(arr)

arr.insert(2,99)#inserts 99 at index 2
print(arr)

arr.remove(15)#removes the first occurrence of 15
print(arr)


arr.pop()#removes the last element of the array
print(arr)
arr.pop(3)#removes the element at index 3
print(arr)


b=arr.index(29)# gives the index of the given index 
print(b)


arr.reverse()#reverses the array
print(arr)


arr.tolist()#converts the array into a list
print(arr)

