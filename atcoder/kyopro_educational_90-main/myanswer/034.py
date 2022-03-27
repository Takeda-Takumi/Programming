n, k = map(int, input().split())
a = list(map(int, input().split()))

r = 0
dict = {}
ans = 0
for l in range(n):
    while(r < n):
        if not a[r] in dict and len(dict) == k:
            break
        if a[r] in dict:
            dict[a[r]] += 1
        else:
            dict[a[r]] = 1
        r += 1
    ans = max(ans, r-l)
    dict[a[l]] -= 1
    if dict[a[l]] == 0:
        del dict[a[l]]
print(ans)

# r = 0
# s = set()
# ans = 0
# for l in range(n):
#     while(r < n and len(s) <= k):
#         s.add(a[r])
#         r += 1
#     ans = max(ans, len(s))

# print(ans)