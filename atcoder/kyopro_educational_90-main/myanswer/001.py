n, l = (int(x) for x in input().split())
k = int(input())
a = [int(x) for x in input().split()]


def isOK(m):
    pre = 0,cnt = 0
    for i in range(0,n):
        if a[i] - pre >= m and l - a[i] >= m:
            cnt += 1
            pre = a[i]
    if cnt >= k:
        return True
    else:
        return False

def binary_search():
    ok = -1
    ng = l + 1
    while abs(ok - ng) > 1:
        mid = int((ok + ng) / 2)
        if(isOK(mid)):
            ok = mid
        else:
            ng = mid
    return ok

print(binary_search())


