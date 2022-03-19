n = int(input())
a = [int(x) for x in input().split()]

dict = {}
for i in range(n):
    dict[a[i]] = i


b = [int(x) for x in input().split()]

ans1 = 0
ans2 = 0
for i in range(n):
    if b[i] in dict:
        if dict[b[i]] == i:
            ans1 += 1
        else:
            ans2 += 1


print(ans1)
print(ans2)