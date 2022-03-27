n, a, b = (int(x) for x in input().split())
p, q, r, s = (int(x) for x in input().split())

ans = [['.']*(s-r+1) for i in range(q-p+1)]

for i in range(p, q+1):
    for j in range(r, s+1):
        if(abs(i-a) == abs(j-b)):
            ans[i-p][j-s] = "#"


for i in range(p, q+1):
    for j in range(r, s+1):
        print(ans[i-p][j-s], end="")
    print()