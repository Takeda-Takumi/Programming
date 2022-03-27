k = int(input())

l = []
for i in range(1, int(k**(0.5))+1):
    if(k % i == 0):
        l.append(i)

ans = 0
for i in range(len(l)):
    for j in range(i, len(l)):
        a = l[i]
        b = l[j]
        if a > b:
            continue
        if k % (a*b) != 0:
            continue
        if k / (a*b) < b:
            continue
        ans += 1

print(ans)
