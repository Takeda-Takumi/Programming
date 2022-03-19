q = int(input())

a = []
ans = []
for i in range(q):
    inp = input().split()
    if len(inp) > 2:
        c, x, k = map(int, inp)
    else:
        c, x = map(int, inp)
    if(c == 1):
        a.append(x)
        a.sort()
    elif(c == 2):
        if a[len(a)-1] < x:
                if len(a) >= k:
                    ans.append(a[len(a)-k])
                    break
                else:
                    ans.append(-1)
        else:
            for j in range(len(a)):
                if a[j] > x:
                    if j-1 >= k:
                        ans.append(a[j-k])
                    else:
                        ans.append(-1)
    elif(c == 3):
        for j in range(len(a)-1, -1, -1):
            if a[j] < x:
                if len(a)-j-1 >= k:
                    ans.append(a[j+k])
                else:
                    ans.append(-1)
    
for x in ans:
    print(x)