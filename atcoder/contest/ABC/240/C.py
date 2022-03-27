n, x = (int(z) for z in input().split())

d = [-1] * (x+1)
d[0] = 0
for i in range(n):
    a, b = (int(z) for z in input().split())
    for j in range(x):
        if(d[j] == i): 
            if(j+a <= x):
                if(d[j+a] < n):
                    d[j+a] = i+1
            if(j+b <= x):
                if(d[j+b] < n):
                    d[j+b] = i+1

if(d[x] == i+1):
    print("Yes")
else:
    print("No")

    