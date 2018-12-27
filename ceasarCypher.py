def isalpha(x):
    if((x >= 'a' and x <= 'z') or (x >= 'A' and x <= 'Z')):
        return 1
    else:
        return 0


str = input("Enter the string ")
n = int(input("Enter the factor of rotation"))
lst = []
for i in range(len(str)):
    x = chr(ord(str[i])+n)
    if(ord(str[i])+n) > 90 and 97 < (ord(str[i])+n) > 122:
        if isalpha(chr(ord(str[i]))):
            lst.append(chr(ord(x)-26+n))
    if isalpha(x):
        lst.append(x)
    else:
        lst.append(str[i])

new = ''.join(lst)
print(new)
