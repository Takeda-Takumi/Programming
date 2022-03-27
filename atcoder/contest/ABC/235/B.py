n = int(input())
h = [int(x) for x in input().split()]

max_hight = h[0]
for i in range(n):
    if(i != n-1 and h[i] < h[i+1]):
        max_hight = h[i+1]
    else:
        break
print(max_hight)

