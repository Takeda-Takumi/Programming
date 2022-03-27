n , w = (int(x) for x in input().split())

a = [0 for i in range(n+1)]
b = [0 for i in range(n+1)]

for i in range(n):
    a[i+1] , b[i+1] = (int(x) for x in input().split())

yammy = [[-1]*(w+1) for i in range(n+1)]

for i in range(n+1):
    for j in range(w+1):
        if(i == 0 or j == 0):
            yammy[i][j] = 0
            continue
        max = -1
        for k in range(1,b[i]+1):
            sueoki = yammy[i-1][j]
            ireru = yammy[i-1][j - k] + a[i]*k
            
            if(j - k < 0):
                value = sueoki
            else:
                if(sueoki > ireru):
                    value = sueoki
                else:
                    value = ireru
            if(max < value):
                max = value
        yammy[i][j] = max

print(yammy[n][w])

