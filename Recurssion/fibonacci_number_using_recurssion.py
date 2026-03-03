n=int(input("Enter which place fibonacci no. you want to print "))
def fibonacci_using_recurssion(n):
    if n==0 or n==1:
        return n
    return fibonacci_using_recurssion(n-1)+fibonacci_using_recurssion(n-2)
print(fibonacci_using_recurssion(n))