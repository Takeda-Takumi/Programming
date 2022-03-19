n = int(input())
s = [input() for _ in range(n)]

f = False

for i in range(n):
    sum = 0
    r = 0
    for j in range(n):   
        while(r < n and sum <= 2):
            if(s[i][r] == '.'):
                sum += 1
            r += 1
        if(r-j >= 5):
            f = True
        if(s[i][j] == '.'):
            sum -= 1

if not f:
    for j in range(n):
        sum = 0
        r = 0
        for i in range(n):   
            while(r < n and sum <= 2):
                if(s[r][j] == '.'):
                    sum += 1
                r += 1
            if(r-i >= 5 and r-j >= 5):
                f = True
            if(s[i][j] == '.'):
                sum -= 1

if not f:
    for i in range(n-5):
        sum = 0
        r = 0
        count = 0
        for j in range(n-5):   
            while(i+r < n and j+r < n and sum <= 2):
                if(s[i+r][j+r] == '.'):
                    sum += 1
                r += 1
            if(r-j >= 5 and r-j >= 5):
                f = True
            if(s[i][j] == '.'):
                sum -= 1

if not f:
    for i in range(n-1, 4, -1):
        sum = 0
        r = 0
        count = 0
        for j in range(n-1, 4, -1):   
            while(i-r < n and j-r < n and sum < 2):
                if(s[i-r][j-r] == '.'):
                    sum += 1
                r += 1
            if(r-j >= 5):
                f = True
            if(s[i][j] == '.'):
                sum -= 1



if(f):
    print("Yes")
else:
    print("No")