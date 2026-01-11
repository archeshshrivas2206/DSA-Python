# counting the digits traditional way
num= 12345
count=0
while num >0:
    num=num//10
    count+=1
print("the amount of digit are ",count)

# Logrithimic way 
from math import *
n=123456789
def Digitcount(n):
    return int(log10(n)+1)
print(Digitcount(n))
