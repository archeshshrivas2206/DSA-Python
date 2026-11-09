s1 = "Archesh Shrivas"
result = ""

for i in s1:
    asc = ord(i)
    if 97 <= asc <= 122:
        result += chr(asc - 32)
    else:
        result += i
print(result)