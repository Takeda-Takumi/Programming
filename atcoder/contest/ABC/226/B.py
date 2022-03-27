n = int(input())
l = [0 for i in range(n)]
a = [[0]*(n) for i in range(n)]
sum_list = [0 for i in range(n)]

for i in range(n):
    inp = [int(x) for x in input().split()]
    l[i] = inp[0]
    sum = 0
    for j in range(l[i]):
        a[i][j] = inp[j+1]
        sum += a[i][j]
    sum_list[i] = sum
    

    

count = 0
for i in range(n-1):
    for j in range(i+1,n):
        if(l[i] == l[j] and sum_list[i] == sum_list[j]):
            ans = 1
            for k in range(l[i]):
                if(a[i][k] != a[j][k]):
                    ans = 0
            count += ans
   
print(n-count)