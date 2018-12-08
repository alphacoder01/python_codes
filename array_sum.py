import array as arr
'''
x = arr.array('i', [])
n = int(input())
for i in range(n):
    y = int(input())
    x.append(y)

print(sum(x))
'''
n = int(input())
a = [int(x) for x in input().split()]
print(sum(a))
