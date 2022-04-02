#!/usr/bin/env python3
import random, string

def randomname(n):
   return ''.join(random.choices(string.ascii_lowercase, k=n))

N = random.randint(1, 100000)
s = randomname(N)

print(N)
print(s)

