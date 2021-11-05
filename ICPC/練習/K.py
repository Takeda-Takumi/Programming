n = int(input())
s = [[] for i in range(n)]
for i in range(n):
    s[i] = input()
for i in range(n):
    print(len(s[i])+1)