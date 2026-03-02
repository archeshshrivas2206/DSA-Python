str=input("enter the string ")
left=0
right=len(str)-1
def palindrome(str,l,r):
    if l>=r:
        return
    palindrome(str,l+1,r-1)
    
