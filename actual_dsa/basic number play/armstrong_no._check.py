n=int(input("Enter the no. "))
tv=n
result=0
nod= len(str(n))
while tv>0:
    ld=tv%10
    result=result+(ld**nod)
    tv=tv//10
if result==n:
    print("The no. is Armstrong! ")
else:
    print("The no. is not Armstrong! ")
    