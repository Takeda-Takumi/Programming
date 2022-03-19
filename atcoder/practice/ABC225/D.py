n, q = map(int, input().split())

back = [-1] * (n+1)
front = [-1] * (n+1)
ans = [[]]
index = 0
for i in range(q):
    inp = [int(x) for x in input().split()]
    c = inp[0]
    if(c == 1):
        x = inp[1]
        y = inp[2]
        back[x] = y
        front[y] = x
    elif(c == 2):
        x = inp[1]
        y = inp[2]
        back[x] = -1
        front[y] = -1
    else:
        x = inp[1]
        cur = x
        while(front[cur] != -1):
            cur = front[cur]

        l = []
        count = 0
        while(cur != -1):
            l.append(cur)
            cur = back[cur]
            count += 1
        
        ans[index].append(count)
        for z in l:
            ans[index].append(z)
        ans.append([])
        index += 1

for a in ans:
    for b in a:
        print(b, "", end = "")
    print()

        
