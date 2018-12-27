'''a = input("Enter you list")#first input list as a string
a = [int(x) for x in a.split(" ")]#convert each element of string to integer
'''

a = list(map(int, input().rstrip().split()))

# b = list(map(int, input().rstrip().split()))

print(a)
