import math
t = int(input())
while t:
    x, y = int(input().split(" "))
    x = int(x)
    y = int(y)

    lcm = int(((x*y)/math.gcd(x, y)))
    print(math.gcd(x, y), lcm)
    t -= 1
