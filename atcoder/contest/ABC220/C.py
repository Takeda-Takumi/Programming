n = int(input())
a = [int(x) for x in input().split()]
x = int(input())

s = [0] * n
s[0] = a[0]
for i in range(1, n):
    s[i] = s[i-1] + a[i]
a_sum = s[n-1]

k = 0
p = x // a_sum
k += p*n

res = x %  a_sum
for i in range(n):
    k += 1
    if(res < s[i]):
        break
    

print(k)
