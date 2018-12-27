'''must read quickstart tutorial of numpy
https://docs.scipy.org/doc/numpy/user/quickstart.html#an-example
'''


import numpy
# do not use numpy as the name of the file as it will create a confusion and the real numpy module will be shadowed under its name and will and work properly.
a = numpy.array([1, 2, 3])
print(a)

print(a.dtype)  # datatype of elements.
print(a.ndim)  # dimension of array.
b = numpy.array([(1.5, 6, 7), (8, 9, 10)])
print(b)

c = numpy.array([(1, 3, 7, 4), (8, 9, 8, 11), (8, 9, 5, 1)], dtype=complex)
print(c)

# returns a flat array i.e converts a n dimension array to 1 dim. array
print(c.ravel())
# returns a modified array of given size , the resize func changes the ori. array.
print(c.reshape(6, 2))
# takes transpose of the original array and returns a modified array.
print(c.T)
'''
The function zeros creates an array full of zeros,
the function ones creates an array full of ones,
and the function empty creates an array whose initial content is random and depends on the state of the memory.
By default, the dtype of the created array is float64
'''

x = numpy.zeros((3, 4))  # array of zeroes by default float64
print(x)

# array of ones but datatype is set to int32
y = numpy.ones((2, 2, 2), int)  # or , dtype=numpy.int32
print(y)

z = numpy.empty((3, 3))  # array of random elemets.
print(z)

# using linspace

j = numpy.linspace(0, 15, 16)  # inluding 15
print(j)

l = numpy.linspace(0, 15)  # by default it breaks into 50 equal parts
print(l)

v = numpy.array([5, 8, 9, 6, 4, 6])
f = numpy.sort(v)
print(f)
