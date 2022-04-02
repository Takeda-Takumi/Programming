#!/usr/bin/env python3
import random
# n = random.randint(1, 2*(10**5))
n = random.randint(1, 10)
# a = [random.randint(1, 10**9) for _ in range(n)]
# b = [random.randint(1, 10**9) for _ in range(n)]
a = [random.randint(1, 10) for _ in range(n)]
b = [random.randint(1, 10) for _ in range(n)]

print(n)
for i in range(n):
    print(a[i], b[i])