a, b, c = map(int, input().split())

tmp = c
while(tmp <= b):
    if(a <= tmp):
        print(tmp)
        break
    tmp += c
else:
    print(-1)