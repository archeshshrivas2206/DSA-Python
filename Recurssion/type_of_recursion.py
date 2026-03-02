#tail recursion parameterised
def ntimeprint(x,n):
    if n<=0:
        return
    print(x)
    ntimeprint(x,n-1)
ntimeprint(69,4)

#head recursion parameterised
def ntimeprinth(x,n):
    if n<=0:
        return
    ntimeprinth(x,n-1)
    print(x)
ntimeprinth(143,4)    

#functional recursion

def sumof(n):
    if n==1:
        return 1
    return n+sumof(n-1)
print(sumof(99))