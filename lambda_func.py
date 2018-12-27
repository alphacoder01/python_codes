'''
def square(a):
    return a*a
    '''
# if a function is neede just once than ,we can use lambda fuction to write the code.


def f(a): return a*a  # a is the argument , a*a is its return value.


'''
f  = lambda a: a*a
after saving it changed to the above statement.
'''

print(f(5))


def k(a, b): return a*b, b-a

'''
k = lambda a,b : a*b,b-a 
'''
print(k(5, 5))

'''
filter , map , reduce
   built in        found in functools module
'''
