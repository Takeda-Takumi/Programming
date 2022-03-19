n = int(input())
a = [int(x) for x in input().split()]
b = [int(x) for x in input().split()]
c = [int(x) for x in input().split()]

am = [0] * 46
bm = [0] * 46
cm = [0] * 46
for i in range(n):
    am[a[i]%46] += 1
    bm[b[i]%46] += 1
    cm[c[i]%46] += 1

ans = 0
for i in range(46):
    for j in range(46):
        for k in range(46):
            if((i + j + k) % 46 == 0):
                ans += am[i] * bm[j] * cm[k]

print(ans)
