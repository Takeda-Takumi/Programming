
while True:

    a = [int(x) for x in input().split()]
    if
    if(a.count(0) == 4):
        exit()

    min_index = 00
    min = 200

    for i in range(4):
        if(a[i] != 0 and a[i] < min):
            min_index = i
            min = a[i]

    for i in range(4):
        if(i == min_index or a[i] == 0):
            continue
        a[i] -= min

    count = 0
    for i in range(4):
        if(a[i] == 0):
            count += 1

    if(count == 3):
        break

print(a[min_index])