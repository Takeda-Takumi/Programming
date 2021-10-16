#import time

n = int(input())
#start = time.time()
if(n % 2 == 0): 
    for i in range(1<<n-1):
        s = ''
        a = 0
        b = 0
        depth = 0
        for j in range(n-1, -1, -1):
            if((b-a) > (j+1)): break
            if((i >> j) & 1):
                if(b == 0): break
                s += ')'
                a += 1
                depth -= 1
            else:
                b += 1
                s += '('
                
                depth += 1
            if(depth < 0): break

        if(a != b): continue
        if(depth == 0): print(s)

#elapsed_time = time.time() - start
#print ("elapsed_time:{0}".format(elapsed_time) + "[sec]")

    

