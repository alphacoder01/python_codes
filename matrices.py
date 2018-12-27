from numpy import *

a = array([(1, 2, 3), (4, 5, 6)])
print(a)

# converting a 2 d array to a matrix

m1 = matrix(a)

# or

m = matrix('1,2,3 ; 4,5,6 ; 1,2,5')
m2 = matrix('23,6,0 ; 9,8,7;0,0,5')
print(m+m2)
print(m*m2)

print(diagonal(m))
print(m.min())  # minimum element
print(m.max())  # maximum element
