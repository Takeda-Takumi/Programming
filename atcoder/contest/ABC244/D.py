s = input()
s = s.replace(' ', '')
t = input()
t = t.replace(' ', '')

dict = {"RGB": 0, "RBG": 1, "GRB": 1, "GBR":2, "BRG":2, "BGR":3}

diff = abs(dict[s] - dict[t])

if diff % 2 == 0:
    print("Yes")
else:
    print("No")

    