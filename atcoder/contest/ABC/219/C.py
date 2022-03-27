x = input()
n = int(input())

dict_x_to_alpha = {}
alpha = "abcdefghijklmnopqrstuvwxyz"
for i in range(26):
    dict_x_to_alpha[x[i]] = alpha[i]

l = []
s = [""] * n

for i in range(n):
    s[i] = input()
    tmp = ""
    for j in range(len(s[i])):
        tmp += dict_x_to_alpha[s[i][j]]
    l.append([tmp, i])

l.sort(key=lambda x:x[0])

for i in range(len(l)):
    print(s[l[i][1]])
