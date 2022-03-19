import math
import random

a, b = (int(x) for x in input().split())

# a = random.randint(1, 10**18)
# b = random.randint(1, 10**18)

# c = math.lcm(a, b)
# if(c > 10**18):
#     print("large")
# else:
#     print(c)

def lcm(x, y):
    a = x
    b = y
    while(b != 0):
        tmp = a
        a = b
        b = tmp % b

    return a

c = lcm(a, b)
# c = math.gcd(a, b)
ans = a * b // c
if(ans > 10**18):
    print("Large")
else:
    print(int(ans))
        