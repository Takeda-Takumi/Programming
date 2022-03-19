n = int(input())
s = input()

atcoder = "atcoder"
j = 0
mod = 10**9 + 7
d = {}

for char in atcoder:
    d[char] = 0

for i in range(n):
    if(s[i] == atcoder[j]):
        d[atcoder[j]] += 1
    elif(j < len(atcoder)-1 and s[i] == atcoder[j+1] and d[atcoder[j]] > 0):
        d[atcoder[j+1]] += 1
        j += 1

ans = 1
for val in d.values():
    if(val > 0):
        ans *= val 
        ans %= mod
    else:
        ans = 0
        break

print(ans)