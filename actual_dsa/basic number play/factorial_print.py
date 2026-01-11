#brute force 
n=int(input("Enter the no."))
factorial=[]
for i in range(1,n+1):
    if n%i==0:
        factorial.append(i)
print("The Factorial of ",n," are ", factorial )

#optimised version
nn=int(input("Enter The no. "))
result=[]
for i in range(1,1+(nn//2) ):
    if nn%i==0:
        result.append(i)
result.append(nn)
print("The Factorial of ",nn," are ", result )

#even more optimal solution 
from math import sqrt
nnn=int(input("Enter the no. "))
fact=[]
for i in range(1,int(sqrt(nnn)+1)):
    if n%i==0:
        fact.append(i)
        if nnn//i !=i:
            fact.append(nnn//i)
print("The Factorial of ",nnn," are ", fact )

