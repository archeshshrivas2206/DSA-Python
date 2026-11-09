string="Archesh"

# built in python feature 
print(string[::-1])

result=""

for i in range(len(string)-1,-1,-1):

    result += string[i]

print (result)

