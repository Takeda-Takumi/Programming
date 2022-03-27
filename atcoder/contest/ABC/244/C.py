n = int(input())

print("1", flush=True)
dict = {}
dict[1] = True

while(True):
    aoki = int(input())
    if aoki == 0:
        exit()
    dict[aoki] = True
    for i in range(1, 2*n+2):
        if i in dict:
            pass
        else:
            print(i, flush=True)
            dict[i] = True
            break
