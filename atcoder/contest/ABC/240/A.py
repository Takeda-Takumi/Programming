a, b = (int(x) for x in input().split())

if abs(a - b) == 1 or abs(a - b) == 9:
    print("Yes")
else:
    print("No")