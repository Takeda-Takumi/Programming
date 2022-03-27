x1, y1, x2, y2 = (int(x) for x in input().split())

d = [[2, 1], [1, 2], [-1, 2], [-2, 1], [-2, -1], [-1, -2], [1, -2], [2, -1]]

ans = "No"
for i in range(len(d)):
    for j in range(len(d)):
        # print(x1+d[i][0], x2+d[j][0], y1+d[i][1], x2+d[j][1])
        if(x1+d[i][0] == x2+d[j][0] and y1+d[i][1] == y2+d[j][1]):
            ans = "Yes"

print(ans)