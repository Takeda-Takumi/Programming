x, y = (int(x) for x in input().split())

if(x >= y):
    print(0)
else:
    print(int((y-x)/10 + ((y-x)%10 > 0)))