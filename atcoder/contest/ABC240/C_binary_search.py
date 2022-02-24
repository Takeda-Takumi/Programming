n, x = (int(z) for z in input().split())

a = [0]*n
b = [0]*n

for i in range(n):
    a[i], b[i] = map(int, input().split())

ans = "No"
for i in range(2**n):
    sum = 0
    for j in range(n):
        if ((i>>j) & 1):
            sum += a[j]
        else:
            sum += b[j]

    if sum == x:
        ans = "Yes"
        break

print(ans)

