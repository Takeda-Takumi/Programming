n = int(input())

x = [0 for i in range(n)]
y = [0 for i in range(n)]

for i in range(n):
    x[i], y[i] = map(int, input().split())


def isTriangle(x1,x2,x3,y1,y2,y3):
    return (((x1 - x2) * (y3 - y2) - (y1 - y2) * (x3 - x2)) != 0)


ans = 0
for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            if(isTriangle(x[i],x[j],x[k],y[i],y[j],y[k])):
                ans += 1

print(ans)
