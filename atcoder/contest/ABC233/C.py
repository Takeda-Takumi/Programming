n, x = (int(x) for x in input().split())

l = [0] * n
a = [[] for i in range(n)] 

for i in range(n):
    inp = input().split()
    l[i] = int(inp[0])
    for j in range(l[i]):
        a[i].append(int(inp[j+1]))

count = [0]*n
ans = 0
f = False
while True:
    if(f):
        break
    mul = 1
    for i in range(n):
        mul *= a[i][count[i]]
    if(mul == x):
        ans += 1

    count[n-1] += 1
    for i in range(1, n+1):
        if(count[n-i] == l[n-i]):
            if(count[0] > l[0]-1):
                f = True
                break
            count[n-i-1] += 1
            count[n-i] = 0


print(ans)