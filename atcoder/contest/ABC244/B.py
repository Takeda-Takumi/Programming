n = int(input())
t = input()

d = [[1, 0], [0, -1], [-1, 0], [0, 1]]

front = 0

x = 0
y = 0
for i in range(n):
    if(t[i] == "S"):
        x += d[front][0]
        y += d[front][1]
    else:
        front += 1
        front %= 4

print(x, y)
