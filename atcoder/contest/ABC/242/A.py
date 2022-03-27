a, b, c, x = (int(x) for x in input().split())

if(x <= a):
    print(float(1))
elif(x > a and x <= b):
    print(float(c/(b-a)))
else:
    print(float(0))