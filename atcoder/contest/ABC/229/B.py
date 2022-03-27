a, b = (x for x in input().split())

n = min(int(len(a)), int(len(b)))
ans = 'Easy'
for i in range(n):
    corrent_a = int(a[len(a)-i-1])
    corrent_b = int(b[len(b)-i-1])
    if(int(a[len(a)-i-1]) + int(b[len(b)-i-1]) >= 10):
        ans = 'Hard'
        break

print(ans)