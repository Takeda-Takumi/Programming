n, k = list(map(int, input().split()))
a = list(map(int, input().split()))
b = list(map(int, input().split()))

sum = 0
for i in range(n):
    sum += abs(a[i] - b[i])
if(k >= sum and (k - sum) % 2 == 0):
        print("Yes")
else:
    print("No")