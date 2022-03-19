n, q = (int(x) for x in input().split())
a = [int(x) for x in input().split()]
p = list(range(n))

ans = []
shift = 0
for i in range(q):
    t, x, y = map(int, input().split())
    x -= 1
    y -= 1
    x = (x + shift) % n
    y = (y + shift) % n
    if(t == 1):
        a[x], a[y] = a[y], a[x]
    elif(t == 2):
        shift += n-1
        shift %= n
    elif(t == 3):
        ans.append(a[x])

for x in ans:
    print(x)
