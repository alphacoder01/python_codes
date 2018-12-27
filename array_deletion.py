# taking array as input
n = int(input("Enter number of elements "))
lst = list(map(int, input().rstrip().split()))
# print(lst)


m = int(input("Enter element to be deleted "))
count = 0
for i in range(n):
    if m != i:
        count += 1
    if count == n:
        m = int(input("Enter a valid number"))
o = int(input("Enter the index "))
lst.pop(o)
print(lst)
