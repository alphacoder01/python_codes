import array as arr

x = arr.array('i', [])
n = int(input())
for i in range(n):
    y = int(input())
    x.append(y)
z = x.tolist()
print(sum(z))
