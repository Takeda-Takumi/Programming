n, m = map(int, input().split())

b = [list(map(int, input().split())) for i in range(n)]

b.insert(0, [])
for i in range(n + 1):
    b[i].insert(0, -1)

tmp = b[1][1]

start_j = tmp % 7
start_i = (tmp - start_j) // 7 + 1


count = 0
for i in range(1, n+1):
    for j in range(1, m+1):
        val = (start_i + (i-1)- 1)*7 + start_j + (j-1)
        if(b[i][j] == val):
            count += 1

if(count == n*m):
    print("Yes")
else:
    print("No")

