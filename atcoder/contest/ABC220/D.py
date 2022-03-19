n = int(input())
a = [int(x) for x in input().split()]

k = [0] * 10
for i in range(10):
    for j in range(10):
        k[(i+j)%10] += 1
        k[(i*j)%10] += 1

print()