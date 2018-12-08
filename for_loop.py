for i in range(1, 11):  # second number is not incluseive
    print("2*{} = {}".format(i, 2*i))

for i in range(1, 25, 2):  # prints numbers from 1 to 50 with gap of 2
    print(i)  # basically odd nos from 1 to 50
    if i == 27:
        break
else:  # used to execute the statements if the break statment didn't got executed
    print("NOT FOUND")

# printing in reverse order

for i in range(20, 0, -1):
    print(i)

# in list
x = ["ashish", 652, 5.5]
for i in x:
    print(i)
