#given 2 list you have to check the frequency of item of second list in first list 
n=[1,9,2,10,3,8,4,7,5,6,1,2,4,6,4,3,6,7,8,9,4,3,2,9]
m=[77,12,2,1,3,4,5,6,7,8,9,67]

hashmap={}
for i in range(0,len(n)):
    hashmap[n[i]]=hashmap.get(n[i],0)+1
for i in range (0,len(m)):
    hashmap[m[i]]=hashmap.get(m[i],0)
    print(m[i],"=", hashmap[m[i]])
    


    '''if m[i] in hashmap:
        print(m[i],"=", hashmap[m[i]])
    else:
        hashmap[m[i]]=0
        print(m[i],"=", hashmap[m[i]])'''
        