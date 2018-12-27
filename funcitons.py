def add_sub(x, y):
    s = x+y
    d = x-y
    return s, d


n = float(input("Enter number 1: "))
m = int(input("Enter number 2: "))
r1, r2 = add_sub(n, m)
print(r1, r2)

# python is neither call by reference nor call by value
# it is rather call by object reference...


def person(name, age=18):  # hre 18 is the default if , we don't provide the second arg. else the age is overriden
    print(name)
    print(age-5)


person("Ashish", 17)
# or
# here we are using the formal arguments as keywords.
person(age=17, name='Ashish')


'''VARIABLE LENGTH ARGUMENT'''
# used when we dont know the no. of aarguments a functin is to receive.


# *a means that its no. is not fixed , it will take all the values passed to the function.
def sum(*a):
    c = 0
    for i in a:
        c = c+i
    print(c)


sum(9, 7, 8, 5, 6)

# also


# it means that we are giving variable length arguments but with kewords attaached.
def people(name, **data):
    print(name)
    for i, j in data.items():  # i,j bcoz one is for keyword and another for the value
        print(i, j)
   # or
   #  print(data)


people('Ashish', age=17, city='meerut')
