h, w = (int(x) for x in input().split())
a = [list(map(int, input().split())) for i in range(h)]

max_h = [0] * h
max_w = [0] * w

for i in range(h):
    for j in range(w):
        max_h[i] += a[i][j]
        max_w[j] += a[i][j]

sum_row_and_columns = [[0]*w for i in range(h)]
for i in range(h):
    for j in range(w):
        sum_row_and_columns[i][j] = max_h[i] + max_w[j] - a[i][j]

for x in sum_row_and_columns:
    print(*x)

