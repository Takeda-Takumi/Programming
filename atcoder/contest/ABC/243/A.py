
v, a, b, c = (int(x) for x in input().split())

ans = ""
while(True):
    if(v >= a):
        v = v - a
    else:
        ans = "F"
        break
    
    if(v >= b):
        v = v - b
    else:
        ans = "M"
        break

    if(v >= c):
        v = v - c
    else:
        ans = "T"
        break

print(ans)
    
    