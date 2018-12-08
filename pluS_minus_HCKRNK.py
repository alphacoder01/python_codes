n = int(input())
a = [int(x) for x in input().split()]
p = m = z = 0
for i in range(len(a)):
    if a[i] > 0:
        p += 1
    elif a[i] < 0:
        m += 1
    else:
        z += 1

print(p/n)
print(m/n)
print(z/n)
