num=[1,3,4,2,2,2,5,6,777,8,9,0,43,777,1,2,3,4,5,6,7,8,9]
dictionary={}
for i in range(0,len(num)):
    if num[i] in dictionary:
        dictionary[num[i]]+=1   
    else:
        dictionary[num[i]]=1
print(dictionary)

#alternate way
nums=[1,3,4,2,2,2,5,6,777,8,9,0,43,777,1,2,3,4,5,6,7,8,9]
hashmap={}
for i in range(0,len(nums)):
    hashmap[nums[i]]=hashmap.get(nums[i],0)+1
print(hashmap)
