# armstrong no. 
#abc :- a no. is equal to sum of individual digit raised to the power of no. of digit of its own 
#abc= a^3+ b^3+ c^3 =abc 

n=int(input("Enter the no. "))
tv=n
digits=[]
while tv>0:
    d=tv%10
    digits.append(d)
    tv=tv//10


