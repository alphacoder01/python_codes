# taking array as input
n = int(input("Enter number of elements "))
lst = list(map(int, input().rstrip().split()))
# print(lst)


m = int(input("Enter element to be insterd "))
o = int(input("Enter the index "))

lst.insert(o, m)
print(lst)
