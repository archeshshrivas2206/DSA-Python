#n=['a','a','b','b','c','c','c','c','e','e','d']
n='vhbodfbvdflhbzlbsdqbdacccaad'
m=['q','b','d','a','c','v','l']

hashmap={}
for i in range(0,len(n)):
    hashmap[n[i]]=hashmap.get(n[i],0)+1
for i in range (0,len(m)):
    hashmap[m[i]]=hashmap.get(m[i],0)
    print(m[i],"=", hashmap[m[i]])