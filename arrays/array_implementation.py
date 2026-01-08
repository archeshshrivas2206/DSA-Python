#the most basic type of data structure is the array
#theres no built-in feature or function to make an array in python
#but we can use lists as arrays
from array import *

arr=array('i',[1,2,3,4,5])#the formula/syntax is variable=array('typecode',[])


print(arr)                #to print the array
print(type(arr))          #to print the type of the array


for i in arr:#{here the i holds the value or arr for each itration}
    print(i)              #to print each element of the array