import itertools

# n = input()

# ans = -1
# for x in itertools.permutations(n):
#     for j in range(1, len(n)):
#         l = 0
#         r = 0
#         for i in range(len(n)):
#             if(i < j):
#                 l = 10*l + int(x[i])
#             else:
#                 r = 10*r + int(x[i])
#         ans = max(ans, l*r)
# print(ans)

n = sorted(input(), reverse=True)
ans = 0

for i in range(1<<len(n)):
    l = 0
    r = 0
    for j in range(len(n)):
        if i & (1<<j):
            l = l*10+ord(n[j])-ord('0')
        else:
            r = r*10+ord(n[j])-ord('0')
        ans = max(ans, l*r)

print(ans)

            
        
