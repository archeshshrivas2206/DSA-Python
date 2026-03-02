str=input("enter the string ")
left=0
right=len(str)-1
def palindrome(str,l,r):
    if l>=r:
        return True
    if str[l]!=str[r]:
        return False
    palindrome(str,l+1,r-1)
    return True
if palindrome(str,left,right)==True:
    print('It is an Palindrome')
else:
    print('It is not an Palindrome')

    
