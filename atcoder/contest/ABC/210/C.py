n, k = map(int, input().split())
c = list(map(int, input().split()))

# dict = {}
# r = 0
# ans = 0
# for l in range(n):
#     pre_r = r
#     while(r < n and not c[r] in dict):
#         dict[c[r]] = 1
#         r += 1
#     if pre_r != r:
#         dict[c[r]] += 1
#     ans = max(ans, len(dict))
#     dict[c[l]] -= 1
#     if dict[c[l]] == 0:
#         del dict[c[l]]
# if ans < k:
#     print(ans)
# else:
#     print(k)

# s = set()
# ans = 0
# for i in range(n-k):
#     for j in range(i,i+k):
#         s.add(c[j])
#     ans = max(ans, len(s))

# print(ans)

r = 0
dict = {}
ans = 0
for l in range(n):
    while(r < n and r - l + 1<= k):
        if c[r] in dict:
            dict[c[r]] += 1
        else:
            dict[c[r]] = 1
        r += 1
    ans = max(ans, len(dict))
    dict[c[l]] -= 1
    if dict[c[l]] == 0:
        del dict[c[l]]

print(ans)


    