n = int(input())
c = [[] for i in range(n)]
p = [[] for i in range(n)]

partial_sum_1 = [[] for i in range(n)]
partial_sum_2 = [[] for i in range(n)]
sum_1 = 0
sum_2 = 0

for i in range(n):
    c[i], p[i] = map(int, input().split())
    if(c[i] == 1):
        sum_1 += p[i]
    else:
        sum_2 += p[i]
        
    partial_sum_1[i] = sum_1
    partial_sum_2[i] = sum_2

q = int(input())
l = [[] for i in range(q)]
r = [[] for i in range(q)]
for i in range(q):
    l[i], r[i] = map(int, input().split())


for i in range(q):
    if(l[i] == 1):
        print(partial_sum_1[r[i]-1], partial_sum_2[r[i]-1])    
    else:
        print(partial_sum_1[r[i]-1] - partial_sum_1[l[i]-2], partial_sum_2[r[i]-1] - partial_sum_2[l[i]-2])


