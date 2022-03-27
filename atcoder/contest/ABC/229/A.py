a , b = (int(x) for x in input().split())

n = min(len(a), len(b))
ans = 'Easy'
for i in range(n):
    if(int(a[len(a)-i-1]) + int(b[len(b)-i-1]) >= 10):
        ans = 'Hard'
        break

    