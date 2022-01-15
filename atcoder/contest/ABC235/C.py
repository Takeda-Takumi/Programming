n, q = (int(x) for x in input().split())
a = [int(x) for x in input().split()]

x = [0] * q
k = [0] * q

for i in range(q):
    x[i], k[i] = (int(x) for x in input().split())


dict = {}
for i in range(n):
    key = a[i]
    if key not in dict:
        dict[key] = []
    dict[key].append(i+1)

for i in range(q):
    # f1 = (x[i] in dict)
    # f2 = (k[i]-1 < len(dict[x[i]]))
    # f3 = k[i] - 1
    # f4 = len(dict[x[i]])
    # f5 = dict[x[i]]
    if (x[i] in dict and k[i]-1 < len(dict[x[i]])):
        print(dict[x[i]][k[i]-1])
    else:
        print(-1)