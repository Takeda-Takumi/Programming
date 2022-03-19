n, x = (int(x) for x in input().split())
s = input()

pos = x
left = 
for i in range(n):
    if s[i] == "U":
        pos = int(pos // 2)
    elif s[i] == "L":
        pos = pos*2
    elif s[i] == "R":
        pos = pos*2 + 1

print(pos)