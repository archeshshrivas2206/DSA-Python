n=123456789
print("Extracted digits in reverse order")
# extracting digigts from a variable in reverse  
num=n
while num > 0:
    last_digit= num%10
    print(last_digit)
    num=num//10
    
# extracting digigts from a variable in actual order 
num3= n
list_of_number=[]
while num3>0:
    last_digit= num3%10
    list_of_number.append(last_digit)
    num3=num3//10
list_of_number.reverse()
print("elements in actual order ")
for i in list_of_number:
    print(i)