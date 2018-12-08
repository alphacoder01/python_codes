a = input("")  # first input list as a string
a = [int(x) for x in a.split(" ")]
b = sorted(a)
min = sum(b) - b[4]
max = sum(b) - b[0]
print(min, end=" ")
print(max)
