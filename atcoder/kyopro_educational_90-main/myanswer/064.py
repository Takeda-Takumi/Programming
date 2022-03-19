from scipy.fftpack import diff


n, q = (int(x) for x in input().split())
a = [int(x) for x in input().split()]

diff = []

fuben = 0
for i in range(n-1):
    diff.append(a[i+1] - a[i])
    fuben += abs(diff[i])

ans = []
for i in range(q):
    l, r, v = (int(x) for x in input().split())
    l -= 1
    r -= 1

    if(l > 0):
        fuben -= abs(diff[l-1])
        diff[l-1] += v
        fuben += abs(diff[l-1])

    if(r < n-1):
        fuben -= abs(diff[r])
        diff[r] += -v
        fuben += abs(diff[r])

    ans.append(fuben)

for x in ans:
    print(x)