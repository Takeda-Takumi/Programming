n = int(input())
a = [int(x) for x in input().split()]

d = {}
count = 0
pre = -1
l = []
for i in range(n):
    l.append(a[i])
    count += 1

    if not a[i] in d:
            d[a[i]] = 1
    if(len(l) != 1):
        if (l[len(l)-1] == l[len(l)-2]):
            d[a[i]] += 1
        else:
            d.pop(pre)
    
    if(d[a[i]] == a[i]):
        count -= a[i]

        d.pop(a[i])
        l = l[:len(l)-a[i]]

    if(len(l) != 0):
        pre = l[len(l)-1]
    else:
        pre = -1

    print(count)