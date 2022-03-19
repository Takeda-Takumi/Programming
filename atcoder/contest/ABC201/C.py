s = input()
maru = 0
batu = 0
for i in range(10):
    if s[i] == "o":
        maru += 1
    elif s[i] == "x":
        batu += 1

hatena = 10-maru-batu
kaijo = [0, 1, 2, 6, 24]
if maru > 4:
    print(0)
else:
    sum = 0
    for i in range(maru, 4+1):
        sum += kaijo[4] / 


    print(ans)