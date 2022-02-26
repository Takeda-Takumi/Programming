
n = int(input())
a = [int(x) for x in input().split()]

all = sum(a)

r = 0
sum = 0
ans = "No"
for i in range(n):
    while(r <= n+i-1 and all/10 > sum):
        sum += a[r%n]
        r += 1
    if(sum == all/10):
        ans = "Yes"
        break
    sum -= a[i]

print(ans)