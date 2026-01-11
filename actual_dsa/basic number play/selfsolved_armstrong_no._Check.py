# armstrong no. 
#abc :- a no. is equal to sum of individual digit raised to the power of no. of digit of its own 
#abc= a^3+ b^3+ c^3 =abc 
#a**x=a*a*a*a......x times 


n=int(input("Enter the no. "))
tv=n
result=0
digits=[]
while tv>0:
    d=tv%10
    digits.append(d)
    tv=tv//10

power=len(digits)
for i in range(0,power):
    result=result+ (digits[i]**power)
    
if n==result:
    print("The number is Armstrong! ")
else:
    print("The no. is not Armstrong")


