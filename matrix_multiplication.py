from numpy import *
n = int(input("Enter the size of matrix: "))
l = []

for i in range(n):
    row_list = []
    for j in range(n):
        row_list.append(int(input()))
    l.append(row_list)

print(l)

m = int(input("Enter the elements of the nxt n*n matrix:\n"))
k = []

for i in range(n):
    row = []
    for j in range(n):
        row.append(int(input()))
    k.append(row)


print(k)


# l = array(l)
# k = array(k)
r = zeros((n,n))


for i in range(n):
    for j in range(n):
        for k in range(n):
            r[i][j] += l[i][k]*k[k][j]
       
print(r)