s = input()

list = []
n = len(s)
for i in range(n):
    new_s = s[1:] + s[0]
    list.append(new_s)
    s = new_s

list.sort()
print(list[0])
print(list[n-1])