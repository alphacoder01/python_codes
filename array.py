# array printing
import array as arr  # to avoid confusion
x = arr.array('i', [5, 9, 8, 7, 5, 3])
# buffer_info() returns address and size of array in a tuple.
print(x.buffer_info())

'''here,
i = integer(signed) -> 2 bytes
I = integer(unsigned) -> 2 bytes
f = signed float -> 4 bytes
d = double integer(signed)  -> 8 bytes
l = long integer(signed) -> 4 bytes
L = long intege(unsigned) -> 4 bytes
'''
x.reverse()
x.append(9)
print(x)


print(x.count(5))  # returns the number of occurences of the element given

print(x.index(8))  # returns add of the first occurence of the element.

# print(x.)  # and lots of functions to work with.


# to print each element of array
# number 1
for i in range(len(x)):
    print(x[i])


# number 2
for e in x:
    print(e)


'''character ARRAY'''
y = arr.array('u', ['a', 'e', 'i', 'o', 'u'])


'''copying a array to new one'''
newArr = arr.array(x.typecode, (a for a in x))  # here if we don't know the type of our array we can use type code and
                                                # for loop is used to fetch each value from old to new array

print(newArr)

# also

new = arr.array(x.typecode,(a*a for a in x))
print(new)                  # prints the square of the values from the old array.