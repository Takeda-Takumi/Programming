import math

n = int(input())

def f(x):
    sum = 0
    tmp = x
    i = 2
    while(i*i <= x):
        if(tmp == 1):
            break
        while(tmp % i == 0):
            sum += 1
            tmp /= i
        i += 1

    if(tmp != x and tmp > 1):
        sum += 1
    return sum

num = f(n)
for i in range(20):
    if((1 << i) >= num):
        print(i)
        break
        
#1000000000000