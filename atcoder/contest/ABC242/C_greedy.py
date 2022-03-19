import math

n = int(input())

start = int("1"*n)
count = 0
i = 0
while(i < 10**n):
    s = str(i)
    s = s.replace('0', '1')
    f = True
    for j in range(len(s)-1):
        if(math.fabs(int(s[j]) - int(s[j+1])) > 1):
            f = False 
    if(f):
        count += 1
    i += 1

print(count)
