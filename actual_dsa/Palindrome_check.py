t=int(input("Enter 1 if number \n Enter 2 if String"))
if t==1:
    n=int(input("Give input"))
    num=n
    result=0
    while num >0:
        ld=num%10
        num= num//10
        result=(result*10)+ld

    if result==n:
        print("The number is palendrome ")
    else :
        print("Not a Palendrom ")
else:
    s=input("Enter the string ")
    #to check for strings
    def ispalendrome(s):
        st=str(s)
        return st==st[::-1]
    print(ispalendrome(s))

