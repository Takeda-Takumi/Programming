#import time

n = int(input())

#start = time.time()
for i in range(1<<n-1):
    s = ''
    a = 0
    b = 0
    for j in range(n-1, -1, -1):
        if((i >> j) & 1):
            if(b == 0): break
            s += ')'
            a += 1
        else:
            s += '('
            b += 1
    if(a != b): continue

    depth = 0
    for j in range(n):
        if(s[j] == '('): depth += 1
        if(s[j] == ')'): depth -= 1
        if(depth < 0): break
    
    if(depth == 0): print(s)

#elapsed_time = time.time() - start
#print ("elapsed_time:{0}".format(elapsed_time) + "[sec]")

    

