h, w = map(int, input().split())
p = [list(map(int, input().split())) for _ in range(h)]


def count(l):
    dist = {}
    ret = 0
    for nx in l:
        if nx in dist:
            dist[nx] += 1
        else:
            dist[nx] = 1
        ret = max(ret, dist[nx])
    return ret

ans = 0
for i in range(1<<h):
    l = []
    for j in range(w):
        val = -1
        f = False
        for k in range(h):   
            if((i>>k) & 1):
                if(val == -1):
                    val = p[k][j]
                if(val != p[k][j]):
                    f = True
        if(f == False):
            l.append(val)
    
    ch = 0
    for j in range(h):
        if((i>>j) & 1):
            ch += 1
    if len(l) > 0:
        ans = max(ans, count(l)*ch)

print(ans)